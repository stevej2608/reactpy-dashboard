from typing import List, Any, Callable, Optional, Union
from pydantic import BaseModel


Updater = Callable[[], None]

RowData = List[Any]

class Column(BaseModel):
    name: str
    style: Optional[str] = None


class TableData(BaseModel):
    rows: RowData = []
    cols: List[Union[str, Column]] = []
