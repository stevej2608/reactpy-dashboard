from typing import Tuple, Callable, List, Any
from pydantic import BaseModel, ValidationError
from reactpy import html, use_state
from reactpy.core.component import Component

from utils.logger import log


class FieldError(ValueError):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)

class FieldModel(BaseModel):
    value: str = None
    error: str = ''


FieldComponent = Callable[[FieldModel, dict,], Component]
Field = Callable[[str, FieldComponent], Component]
Form = Callable[[*List[Component]], Component]


def create_model(model:BaseModel) -> dict[str, FieldModel]:
    fields = {}

    for name, value in model.dict().items():
        fields[name] = [value, ""]

    return fields


def model_values(form_state: dict[str, FieldModel]) -> dict[str, Any]:
    fields = {}
    for name, state in form_state.items():
        fields[name] = state[0]
    return fields


def createForm(model: BaseModel, set_model) -> Tuple[Form, Field]:

    form_state, set_form_state = use_state(create_model(model))

    def _field(name, fn) -> Component:

        def onchange(event):

            value, error = form_state[name]
            value = event['currentTarget']['value']

            log.info('onchange %s=%s', name, value)

            try:

                # Use the latest field value to create a new model. This
                # will invoke any model field validators

                form_values = model_values(form_state)
                form_values[name] = value
                m = type(model)(**form_values)

                # No complaints from the validators, new data
                # must be OK, update the user model and form values

                set_model(m)

            except ValidationError as ex:
                message = ex.args[0][0].exc.message
                error = message

            form_state[name] = [value, error]

            log.info('set_form_state %s=%s', name, form_state)
            set_form_state(form_state)


        log.info('get_form_state %s=%s', name, form_state)
        value, error = form_state[name]

        def _props(props):
            props['name'] = name
            props['onchange'] = onchange

            if value is not None:
                props['value'] = value

            return props

        form_input = fn(FieldModel(value=value, error=error), _props)
        return form_input

    def _form(*children: List[Component]):
        return html.form(*children)

    return [_form, _field]
