from typing import Tuple, Callable, List, Any, Dict
from pydantic import BaseModel, ValidationError
from reactpy import html, use_state
from reactpy.core.component import Component

from utils.logger import log


class FieldError(ValueError):
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


# class FormModel:

#     def __init__(self, state: BaseModel):
#         self.state = state
#         self.fields = {}

#         for name, value in state.dict().items():
#             self.fields[name] = FieldModel(value=value)

#     def get_field(self, name:str) -> FieldModel:
#         return self.fields[name]


class FormModel(BaseModel):
    state: BaseModel
    fields: Dict[str, FieldModel] = []



def create_model(state: BaseModel, fields: dict = None, update: FieldModel = None) -> FormModel:

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


def form_state(state: BaseModel):
    model = create_model(state)
    form_model, set_model = use_state(model)
    return [form_model, set_model]


def createForm(model: BaseModel, set_model) -> Tuple[Form, Field]:

    def _field(name, fn) -> Component:

        def onchange(event):

            field_model = model.fields[name]

            field_model.value = event['currentTarget']['value']
            field_model.error = ''

            log.info('****** onchange %s: [%s] *****', name, field_model)

            try:

                # Save the new internal state

                set_model(model)

                # Update the user model (this my fail validation)

                new_model = create_model(model.state, model.fields, update=field_model)
                set_model(new_model)

                log.info('model updated %s: [%s]', name, new_model)

            except ValidationError as ex:

                log.info('validation error %s: [%s]', name, field_model)

                # Return the user model to its previous state and set the error

                new_model = create_model(model.state, model.fields)

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
