from typing import Tuple, Callable, List, overload, TypeVar, Dict, Any, cast, Union, Protocol
from pydantic import ValidationError
from reactpy import html, event, use_state
from reactpy.core.component import Component
from reactpy.core.hooks import current_hook
from reactpy.core.types import State
from reactpy.core.types import VdomDict
from utils.logger import log
from utils.types import EventArgs, Props

from reactpy_forms.field_model import FieldModel, FieldValidationError
from reactpy_forms.form_model import FormModel

FieldComponent = Callable[[FieldModel, Dict[Any, Any]], Component]
Field = Callable[[str, FieldComponent], Component]
Form = Callable[[List[Component]], Component]

# pylint: disable=protected-access
# pyright: reportPrivateUsage=false

TModel = TypeVar("TModel", bound=FormModel)

@overload
def use_form_state(initial_value: Callable[[], TModel]) -> State[TModel]:
    ...


@overload
def use_form_state(initial_value: TModel) -> State[TModel]:
    ...



def use_form_state(initial_value: TModel | Callable[[], TModel]) -> State[TModel]:
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

    model, dispatch = use_state(cast(TModel,initial_value))

    # TODO - change LifeCycleHook to make ._rendered_atleast_once accessible

    if not current_hook()._rendered_atleast_once: #noqa
        model.init_field_model()

    return State(model, dispatch)

class FormFunc(Protocol):
    def __call__(self, *argv:Any, **kwarg: Dict[str, Any]) -> VdomDict: ...

class FieldFunc(Protocol):
    def __call__(self, name:str, fn:Callable[[Any, Any], Any]) -> Component: ...

UserModel = TypeVar('UserModel', bound=FormModel)

SetModelFunc = Callable[[Union[UserModel, Callable[[UserModel],UserModel]]],None]

def createForm(model: FormModel, set_model: SetModelFunc[UserModel]) -> Tuple[FormFunc, FieldFunc]:
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


        model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))

        Form, Field = createForm(model, set_model)
        return Form(
            Field('email', lambda field, props: html.input(props({'type':'email'}))),
            Field('password', lambda field, props: html.input(props({'type': 'password'})))
            )

    ```
    """

    def _field(name:str, fn:Callable[[Any, Any], Any]) -> Component:

        if not model.has_field(name):
            raise FieldValidationError(f'Field "{name}" is not defined in the form model')

        # TODO: extract common code from event handlers

        @event(prevent_default=True)
        def onchange(event: EventArgs):

            field_model = model.get_field(name)

            field_model.value = event['currentTarget']['value']
            field_model.error = ''

            # log.info('onchange [%s]', field_model)

            try:

                # Update the model (this may fail validation)

                new_model = FormModel.update_model(model, update=field_model)

                # Inputs must be valid, update the external model

                set_model(new_model)


            except ValidationError as ex:

                # log.info('validation error [%s]', field_model)

                # Return the model to its previous state and set the error

                new_model = FormModel.update_model(model)

                # Update the field model with the value and the validation error.

                field_model.error = ex.args[0][0].exc.message
                new_model.set_field(field_model)

                # Update the external state

                set_model(new_model)

        @event(prevent_default=True)
        def onclick(event: EventArgs):
            field_model = model.get_field(name)
            # log.info('get_field_state [%s]', field_model)

            if isinstance(field_model.value, bool):
                field_model.value = not field_model.value
            else:
                raise FieldValidationError(f'Field "{name}" must be a bool type')

            try:

                # Update the model (this may fail validation)

                new_model = FormModel.update_model(model, update=field_model)

                # Inputs must be valid, update the external model

                set_model(new_model)

            except ValidationError:
                log.info('validation error [%s]', field_model)


        field_state = model.get_field(name)

        def _props(props: Union[Props, None]=None):

            if props is None:
                props = {}

            props['name'] = name

            if 'type' in props and props['type'] in ['button', 'checkbox','radio','reset','submit']:
                props['onclick'] = onclick
            else:
                props['onchange'] = onchange
                if field_state.value is not None:
                    props['value'] = field_state.value

            return props

        form_input = fn(field_state, _props)
        return form_input

    def _form(*argv:Any, **kwarg: Dict[str, Any]) -> VdomDict:
        return html.form(*argv, **kwarg)

    # return [_form, _field]
    return (_form, _field)
