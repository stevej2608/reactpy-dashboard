from typing import Tuple, Callable, List, TypeVar
from pydantic import BaseModel, ValidationError
from reactpy import html, use_state
from reactpy.core.component import Component

from utils.logger import log
# from reactpy_forms.model import FieldModel, FormModel

# Loosly based on modularforms:
#       https://modularforms.dev/solid/guides/create-your-form

# https://docs.pydantic.dev/1.10/usage/validators/

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


def createForm(model: BaseModel, set_model) -> Tuple[Form, Field]:

    log.info('createForm')

    form_values, set_form_values = use_state(model.dict())


    def _field(name, fn) -> Component:

        field_model, set_field_model = use_state(FieldModel(value=form_values[name]))

        log.info('_field %s=%s', name, field_model.value)

        def onchange(event):

            # Update the internal model values state

            value = event['currentTarget']['value']
            error = ''

            try:

                # Use the latest field values to create a new model. This
                # will invoke the model field validators

                form_values[name] = value
                m = type(model)(**form_values)

                # No complaints from the validators, new data
                # must be OK update the user model and form values

                set_model(m)
                set_form_values(m.dict())

            except ValidationError as ex:
                message = ex.args[0][0].exc.message
                log.info('Field %s, value=%s - error %s', name, value, message)
                error = message

            set_field_model(FieldModel(value=value, error=error))


        def _props(props):
            log.info('_props %s', name)
            props['name'] = name
            props['onchange'] = onchange

            if field_model.value is not None:
                props['value'] = field_model.value

            return props

        form_input = fn(field_model, _props)
        return form_input

    def _form(*children: List[Component]):
        return html.form(*children)

    return [_form, _field]
