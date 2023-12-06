from typing import List, Callable, Any, Tuple, Optional
from abc import abstractmethod
from pydantic import BaseModel




class TableData(BaseModel):
    rows: List[Any] = []


Updater = Callable[[BaseModel, BaseModel], None]

class Plugin(BaseModel):
    table: TableData
    updater: Callable[[BaseModel,BaseModel], None]


class RowModel(Plugin):
    ...


class Paginator(Plugin):

    page_index: int = 0
    page_size: int

    @property
    @abstractmethod
    def rows(self): ...

    @property
    @abstractmethod
    def page_count(self): ...

    @abstractmethod
    def first_page(self): ...

    @abstractmethod
    def previous_page(self): ...

    @abstractmethod
    def next_page(self): ...

    @abstractmethod
    def last_page(self): ...

    @abstractmethod
    def get_can_previous_page(self) -> bool: ...

    @abstractmethod
    def get_can_next_page(self) -> bool: ...



class Table(BaseModel):

    data: TableData
    paginator: Optional[Paginator] = None
    row_model: Optional[RowModel] = None


PluginFactory = Callable[[Table, Updater], None]


class Options(BaseModel):
    data: List[Any] = []
    cols: List[str] = []
    plugins: List[PluginFactory] = []
