from typing import Any
from pydantic import BaseModel




class FieldValidationError(ValueError):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)


class FieldModel(BaseModel):
    name: str
    value: Any = None
    error: str = ''
