from typing import List, Any
from pydantic import BaseModel


class TableData(BaseModel):
    rows: List[Any] = []
