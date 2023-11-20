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
    form_model: BaseModel
    field_model: Dict[str, FieldModel] = []

    @staticmethod
    def create_model(form_model: BaseModel, field_model: Dict[str, FieldModel] = None, update: FieldModel = None) -> TypeVar('FormModel'):
        """Create an initial FieldModel or copy/update the existing internal FieldModel

        Args:
            form_model (BaseModel): The user model..
            field_model  Dict[str, FieldModel]): The internal mfield

        Returns:
            FormModel:The composite form & firld modle
        """

        field_model = field_model if field_model else {}

        for name, value in form_model.dict().items():

            if update and update.name == name:
                field_model[name] = update.copy()

            if name not in field_model:
                field_model[name] = FieldModel(name=name, value=value)

        # Update the user model

        if update:
            values = form_model.dict()
            values[update.name] = update.value
            form_model = type(form_model)(**values)

        return FormModel(form_model=form_model, field_model=field_model)


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
    model = FormModel.create_model(initial_value)
    form_model, set_model = use_state(model)
    return [form_model, set_model]


def createForm(model: FormModel, set_model) -> Tuple[Form, Field]:
    """Accept the model and setter created by use_form_state() and return
    the Form & Field HOC's that will be used to wrap the form elements

    Args:
        model (FormModel): Form model created by use_form_state()
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

            field_model = model.field_model[name]

            field_model.value = event['currentTarget']['value']
            field_model.error = ''

            log.info('****** onchange %s: [%s] *****', name, field_model)

            try:

                # Update the user model (this may fail validation)

                new_model = FormModel.create_model(model.form_model, model.field_model, update=field_model)
                set_model(new_model)

                log.info('model updated %s: [%s]', name, new_model)

            except ValidationError as ex:

                log.info('validation error %s: [%s]', name, field_model)

                # Return the user model to its previous state and set the error

                new_model = FormModel.create_model(model.form_model, model.field_model)

                field_model.error = ex.args[0][0].exc.message
                new_model.field_model[name] = field_model

                set_model(new_model)

                log.info('model reverted %s: [%s]', name, new_model)


        field_state = model.field_model[name]

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
