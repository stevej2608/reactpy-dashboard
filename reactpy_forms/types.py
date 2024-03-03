from typing import Callable, List, Dict, Any, Union, Protocol
from reactpy.core.component import Component
from reactpy.core.types import VdomDict

from reactpy_forms.field_model import FieldModel
from reactpy_forms.form_model import TFormModel

FieldComponent = Callable[[FieldModel, Dict[Any, Any]], Component]
Field = Callable[[str, FieldComponent], Component]
Form = Callable[[List[Component]], Component]


class FormFunc(Protocol):
    def __call__(self, *argv:Any, **kwarg: Dict[str, Any]) -> VdomDict: ...


class FieldFunc(Protocol):
    def __call__(self, name:str, fn:Callable[[Any, Any], Any]) -> Component: ...


SetModelFunc = Callable[[Union[TFormModel, Callable[[TFormModel],TFormModel]]],None]
