from typing import List, Callable, Any, Tuple, TypeVar
from pydantic import BaseModel


class RowModel(BaseModel):
    rows: List[Any] = None

class ReactpyTable:

    def __init__(self, table_data: Any):
        self.table_data = table_data

    def test(self):
        return True

PluginFactory = Callable[[ReactpyTable], Tuple[str, TypeVar('Plugin')]]

class Options(BaseModel):
    data: Any = None
    cols: List[str] = None
    plugins: List[PluginFactory]
