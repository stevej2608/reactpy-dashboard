from typing import List, Any
from pydantic import BaseModel

RowData = List[Any]

class TableData(BaseModel):
    rows: RowData = []
