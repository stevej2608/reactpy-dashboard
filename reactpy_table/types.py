from typing import List, Callable, Any, Tuple, TypeVar, Optional, List
from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


TableData = List[Any]


class RowModel(BaseModel):
    rows: List[Any] = []


class AbstractTable(metaclass=ABCMeta):

    @property
    @abstractmethod
    def table_data(self) -> TableData:
        ...

    @abstractmethod
    def set_table(self, table: 'AbstractTable'):
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

PluginFactory = Callable[[AbstractTable], Tuple[str, AbstractPlugin]]

class Options(BaseModel):
    data: Any = None
    cols: List[str] = []
    plugins: List[PluginFactory] = []
