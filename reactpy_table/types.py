from typing import List, Callable, Any, Tuple, Optional
from abc import abstractmethod
from pydantic import BaseModel




class TableData(BaseModel):
    rows: List[Any] = []


class Plugin(BaseModel):

    table: TableData



class RowModel(Plugin):
    ...


class Paginator(Plugin):

    page_index: int = 0
    page_size: int


    @property
    @abstractmethod
    def page_count(self): ...

    @abstractmethod
    def first_page(self): ...

    @abstractmethod
    def previous_page(self): ...



class Table(BaseModel):

    data: TableData
    paginator: Optional[Paginator] = None
    row_model: Optional[RowModel] = None

PluginFactory = Callable[[Table], Table]


class Options(BaseModel):
    data: List[Any] = []
    cols: List[str] = []
    plugins: List[PluginFactory] = []
