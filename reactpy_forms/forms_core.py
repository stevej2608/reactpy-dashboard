from typing import Tuple, Callable, List, Dict, overload, TypeVar
from pydantic import BaseModel, ValidationError
from reactpy import html, use_state
from reactpy.core.component import Component
from reactpy.core.types import State


from utils.logger import log


class FieldValidationError(ValueError):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)


class FieldModel(BaseModel):
    name: str
    value: str = None
    error: str = ''


FieldComponent = Callable[[FieldModel, dict,], Component]
Field = Callable[[str, FieldComponent], Component]
Form = Callable[[*List[Component]], Component]


class FormModel(BaseModel):
    """Container for the Pydantic form model supplied by the 
    user and a field model that is created and 
    managed internally. 
    """
    state: BaseModel
    fields: Dict[str, FieldModel] = []


def _create_model(state: BaseModel, fields: dict = None, update: FieldModel = None) -> FormModel:

    # Create/update the internal files

    fields = fields if fields else {}

    for name, value in state.dict().items():

        if name not in fields:
            fields[name] = FieldModel(name=name, value=value)

        if update and update.name == name:
            fields[name] = update.copy()

    # Update the user model

    if update:
        values = state.dict()
        values[update.name] = update.value
        state = type(state)(**values)

    return FormModel(state=state, fields=fields)


_Type = TypeVar("_Type")

@overload
def use_form_state(initial_value: Callable[[], _Type]) -> State[_Type]:
    ...


@overload
def use_form_state(initial_value: _Type) -> State[_Type]:
    ...


def use_form_state(initial_value: _Type | Callable[[], _Type]) -> State[_Type]:
    """Create a form state model. Used in the same way
    as the reactpy hooks.use_state

    Parameters:
        initial_value:
            Defines the initial value of the state. A callable (accepting no arguments)
            can be used as a constructor function to avoid re-creating the initial value
            on each render.

    Returns:
        A tuple containing the current state and a function to update it.
    """
    model = _create_model(initial_value)
    form_model, set_model = use_state(model)
    return [form_model, set_model]


def createForm(model: BaseModel, set_model) -> Tuple[Form, Field]:
    """Accept the model and setter created by use_form_state() and return
    the Form & Field HOC's that will be used to wrap the form elements

    Args:
        model (BaseModel): Form model created by use_form_state()
        set_model (Callable): Model setter created by use_form_state()

    Returns:
        Tuple[Form, Field]: Form & Field HOC's that will be used to wrap the form elements


    Usage:
    ```
        from pydantic import BaseModel

        class LoginFormData(BaseModel):
            email: str = None
            password: str = None


        model, set_model = use_form_state(LoginFormData(email="jones@gmail.com", password="passme99"))

        Form, Field = createForm(model, set_model)
        return Form(
            Field('email', lambda field, props: html.input(field, props({'type':'email'}))),
            Field('password', lambda field, props: html.input(props({'type': 'password'})))
            )

    ```
    """

    def _field(name, fn) -> Component:

        def onchange(event):

            field_model = model.fields[name]

            field_model.value = event['currentTarget']['value']
            field_model.error = ''

            log.info('****** onchange %s: [%s] *****', name, field_model)

            try:

                # Update the user model (this may fail validation)

                new_model = _create_model(model.state, model.fields, update=field_model)
                set_model(new_model)

                log.info('model updated %s: [%s]', name, new_model)

            except ValidationError as ex:

                log.info('validation error %s: [%s]', name, field_model)

                # Return the user model to its previous state and set the error

                new_model = _create_model(model.state, model.fields)

                field_model.error = ex.args[0][0].exc.message
                new_model.fields[name] = field_model

                set_model(new_model)

                log.info('model reverted %s: [%s]', name, new_model)


        field_state = model.fields[name]

        log.info('get_field_state %s: [%s]', name, field_state)

        def _props(props):
            props['name'] = name
            props['onchange'] = onchange

            if field_state.value is not None:
                props['value'] = field_state.value

            return props

        form_input = fn(field_state, _props)
        return form_input

    def _form(*children: List[Component]):
        return html.form(*children)

    return [_form, _field]
