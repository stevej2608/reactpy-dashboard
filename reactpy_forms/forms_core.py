from typing import Tuple, Callable, List, overload, TypeVar
from pydantic import ValidationError
from reactpy import html, event, use_state
from reactpy.core.hooks import _use_const, _CurrentState
from reactpy.core.component import Component
from reactpy.core.types import State
from utils.logger import log

from reactpy_forms.field_model import FieldModel
from reactpy_forms.form_model import FormModel

FieldComponent = Callable[[FieldModel, dict,], Component]
Field = Callable[[str, FieldComponent], Component]
Form = Callable[[*List[Component]], Component]


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

    model, dispatch = use_state(initial_value)

    if model.is_empty():
        model.init_field_model()

    return [model, dispatch]

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


        model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))

        Form, Field = createForm(model, set_model)
        return Form(
            Field('email', lambda field, props: html.input(props({'type':'email'}))),
            Field('password', lambda field, props: html.input(props({'type': 'password'})))
            )

    ```
    """

    def _field(name, fn) -> Component:

        @event(prevent_default=True)
        def onchange(event):

            field_model = model.get_field(name)

            field_model.value = event['currentTarget']['value']
            field_model.error = ''

            log.info('onchange [%s]', field_model)

            try:

                # Update the model (this may fail validation)

                new_model = FormModel.update_model(model, update=field_model)

                # Inputs must be valid, update the external model

                set_model(new_model)


            except ValidationError as ex:

                log.info('validation error [%s]', field_model)

                # Return the model to its previous state and set the error

                new_model = FormModel.update_model(model)

                # Update the field model with the value and the validation error.

                field_model.error = ex.args[0][0].exc.message
                new_model.set_field(field_model)

                # Update the external state

                set_model(new_model)

        @event(prevent_default=True)
        def onclick(event):
            field_model = model.get_field(name)
            log.info('get_field_state [%s]', field_model)

            field_model.value += 1

            try:

                # Update the model (this may fail validation)

                new_model = FormModel.update_model(model, update=field_model)

                # Inputs must be valid, update the external model

                set_model(new_model)

            except ValidationError:
                log.info('validation error [%s]', field_model)


        field_state = model.get_field(name)

        def _props(props):
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

    def _form(*children: List[Component]):
        return html.form(*children)

    return [_form, _field]
