from typing import Tuple, Callable, List, TypeVar
from pydantic import BaseModel
from reactpy import html, use_state
from reactpy.core.component import Component

from utils.logger import log

# Loosly based on modularforms:
#       https://modularforms.dev/solid/guides/create-your-form

# https://docs.pydantic.dev/1.10/usage/validators/


class FieldData:

    @property
    def value(self):
        model = self.model.todict()
        return model[self.field_name]

    def __init__(self, field_name:str, model: TypeVar('FormModel')):
        self.field_name = field_name
        self.model = model
        self.error = False
        self.exception = None

    def update_model(self, value):
        try:
            # If this fails we have a validation error

            self.model.copy_model(update={self.field_name : value})

            # All OK, update the actual model

            self.model.update_model(update={self.field_name : value})
            self.error = False
        except Exception as ex:
            log.info('Field %s, value=%s - error %s', self.field_name, value, ex)
            self.error = True
            self.exception = ex


class FormModel:

    def __init__(self, form: BaseModel):
        self._model = form
        self._fields = []

    def todict(self) -> dict:
        return self._model.dict()

    def copy_model(self, *args, **kwargs) -> BaseModel:
        return self._model.copy(*args, **kwargs)


    def update_model(self, *args, **kwargs) -> None:
        """Recreate the model using the current values. Any pydantic
        validators will throw an exception if the data is invalid
        """
        model = self.copy_model(*args, **kwargs)
        values = model.dict()

        self._model = type(model)(**values)


    def add_field(self, name: str):

        if self.has_field(name):
            raise ValueError(f"Field name={name} allready exists")

        if name in self._model.dict():
            field = FieldData(name, self)
            self._fields.append(field)
            return field
        else:
            raise ValueError(f"Field name={name} is not in data model")


    def has_field(self, name: str):
        for field in self._fields:
            if field.field_name == name:
                return True
        return False
    
    def __repr__(self): 
        return str(self._model)

FieldComponent = Callable[[FieldData, dict,], Component]

Field = Callable[[str, FieldComponent], Component]

Form = Callable[[*List[Component]], Component]


def createForm(form: BaseModel) -> Tuple[Form, Field, FormModel]:
    """
    
    The returned Form, Field and FieldArray component are connected with the store of 
    your form. They are aware of your fields and their data types, which 
    gives you the benefit of type safety and autocompletion

    Args:
        form (BaseModel): _description_

    Returns:
        Tuple[str, Component, float]: _description_
    """

    log.info('createForm')

    form_model = FormModel(form)

    _field = None

    def _field(name, fn) -> Component:

        log.info('_field %s', name)

        field_data = form_model.add_field(name)

        field_value, set_field = use_state(field_data.value)

        def onchange(event):
            value = event['currentTarget']['value']
            log.info('%s.onchange(value=%s)', name, value)
            field_data.update_model(value)
            set_field(field_data.value)

        def _props(props):
            log.info('_props %s', name)
            props['name'] = name
            props['onchange'] = onchange

            if field_value is not None:
                props['value'] = field_value

            return props

        form_input = fn(field_data, _props)
        return form_input

    def _form(*children: List[Component]):
        return html.form(*children)

    return [_form, _field, form_model]
