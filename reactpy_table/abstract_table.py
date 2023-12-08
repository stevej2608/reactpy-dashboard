from typing import Optional
from pydantic import BaseModel

from .table_data import TableData

from .abstract_row_model import RowModel
from .abstract_paginator import Paginator
from .abstract_column_sort import ColumnSort
from .abstract_table_search import TableSearch


class Table(BaseModel):

    data: TableData

    paginator: Optional[Paginator] = None
    sort: Optional[ColumnSort] = None
    search: Optional[TableSearch] = None
    row_model: Optional[RowModel] = None
