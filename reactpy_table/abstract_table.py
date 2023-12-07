from typing import List, Callable, Any, Optional
from pydantic import BaseModel

from .table_data import TableData
from .abstract_plugin import Updater
from .abstract_row_model import RowModel
from .abstract_paginator import Paginator


class Table(BaseModel):

    data: TableData
    paginator: Optional[Paginator] = None
    row_model: Optional[RowModel] = None


PluginFactory = Callable[[Table, Updater], None]


class Options(BaseModel):
    data: List[Any] = []
    cols: List[str] = []
    plugins: List[PluginFactory] = []
