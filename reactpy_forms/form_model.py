from typing import Dict, TypeVar
from pydantic import BaseModel

from reactpy_forms.field_model import FieldModel


class FormModel(BaseModel):
    """Container for the Pydantic form model supplied by the 
    user and a field model that is created and 
    managed internally. 

    The form_model and the field_model are updated with the inputs from 
    the UI. The form_model values are the last fully validated inputs. 
    
    The field_model holds the unvalidated input. When a validation error
    occurs the field_model will hold the erroneous value. Erroneous values
    are not propagated to the user accessible form_model.

    """

    _field_model: Dict[str, FieldModel] = {}


    def init_field_model(self) -> None:
        """Create an initial FieldModel"""

        for name, value in self.dict().items():
            self._field_model[name] = FieldModel(name=name, value=value)


    def get_model(self) -> Dict[str, FieldModel]:
        return self._field_model


    def set_model(self, model:Dict[str, FieldModel]) -> None:
        for name, value in model.items():
            self._field_model[name] = value

    def get_field(self, name:str) -> FieldModel:
        return self._field_model[name].copy()


    def set_field(self, field:FieldModel):
        self._field_model[field.name] = field


    def is_empty(self) -> bool:
        return not self._field_model


    @staticmethod
    def update_model(model: BaseModel, update: FieldModel= None) -> TypeVar('FormModel'):
        """Copy and update the existing internal FieldModel

        Args:
            model (BaseModel): The model to be updated

        Returns:
            FormModel:The composite form & field model
        """

        field_model = model.get_model()

        for name in model.dict():

            if update and update.name == name:
                field_model[name] = update.copy()

        # Update the user model

        if update:
            values = model.dict()
            values[update.name] = update.value
            user_model = type(model)(**values)
        else:
            user_model = model.copy()

        user_model.set_model(field_model)

        return user_model
