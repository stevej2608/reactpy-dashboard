from typing import List, Any, Callable
from pydantic import BaseModel


Updater = Callable[[], None]

PluginFactory = Callable[['TableData', Updater], None]

RowData = List[Any]


class Options(BaseModel):
    data: RowData = []
    cols: List[str] = []
    plugins: List[PluginFactory] = []


class TableData(BaseModel):
    data: RowData = []
    options: Options
