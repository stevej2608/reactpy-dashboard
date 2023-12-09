from typing import List, Any, Callable, Optional, Union
from pydantic import BaseModel


Updater = Callable[[], None]

RowData = List[Any]

class Column(BaseModel):
    name: str
    label: str
    style: Optional[str] = None
    sort : Optional[Callable[['Column'], None]] = None
    width: str = ""



Columns = List[Column]

class TableData(BaseModel):
    rows: RowData = []
    cols: Columns = []

