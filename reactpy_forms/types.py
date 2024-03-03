from typing import Callable, List, TypeVar, Dict, Any, Union, Protocol
from reactpy.core.component import Component
from reactpy.core.types import VdomDict

from reactpy_forms.field_model import FieldModel
from reactpy_forms.form_model import FormModel

FieldComponent = Callable[[FieldModel, Dict[Any, Any]], Component]
Field = Callable[[str, FieldComponent], Component]
Form = Callable[[List[Component]], Component]


TModel = TypeVar("TModel", bound=FormModel)
UserModel = TypeVar('UserModel', bound=FormModel)

class FormFunc(Protocol):
    def __call__(self, *argv:Any, **kwarg: Dict[str, Any]) -> VdomDict: ...


class FieldFunc(Protocol):
    def __call__(self, name:str, fn:Callable[[Any, Any], Any]) -> Component: ...


SetModelFunc = Callable[[Union[UserModel, Callable[[UserModel],UserModel]]],None]
