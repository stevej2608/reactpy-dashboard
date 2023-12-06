from typing import List, Callable, Any, Optional
from abc import abstractmethod
from pydantic import BaseModel


class TableData(BaseModel):
    rows: List[Any] = []


Updater = Callable[[], None]

class Plugin(BaseModel):
    table: TableData
    updater: Updater


class RowModel(Plugin):
    ...

