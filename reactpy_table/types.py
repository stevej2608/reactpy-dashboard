from typing import List, Callable, Any, Tuple, TypeVar, Optional
from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class RowModel(BaseModel):
    rows: List[Any] = []


class ReactpyTableBase(metaclass=ABCMeta):
    ...


class AbstractPlugin(metaclass=ABCMeta):
    ...


class AbstractPaginator(metaclass=ABCMeta):

    @abstractmethod
    def first_page(self): ...

    @abstractmethod
    def previous_page(self): ...

class AbstractRowModel(metaclass=ABCMeta):
    ...

PluginFactory = Callable[[ReactpyTableBase], Tuple[str, AbstractPlugin]]

class Options(BaseModel):
    data: Any = None
    cols: List[str] = []
    plugins: List[PluginFactory] = []
