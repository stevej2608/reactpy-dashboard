from typing import TypeVar
from pydantic import BaseModel


from utils.logger import log

# Loosly based on modularforms:
#       https://modularforms.dev/solid/guides/create-your-form

# https://docs.pydantic.dev/1.10/usage/validators/


class FieldModel:

    @property
    def value(self):
        model = self.form_model.todict()
        return model[self.field_name]


    @property
    def last_value(self):
        return self._last_value


    def __init__(self, field_name:str, form_model: TypeVar('FormModel')):
        self.field_name = field_name
        self.form_model = form_model
        self.error = False
        self.exception = None
        self._last_value = None


    def update_model(self, value)-> BaseModel:

        self._last_value = value

        try:
            # If this fails we have a validation error

            self.form_model.copy_model(update={self.field_name : value})

            # All OK, update the actual model

            self.form_model.update_model(update={self.field_name : value})
            self.error = False

        except Exception as ex:
            log.info('Field %s, value=%s - error %s', self.field_name, value, ex)
            self.error = True
            self.exception = ex

        return self.form_model.model


class FormModel:

    @property
    def model(self):
        return self._model

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
            field = FieldModel(name, self)
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
