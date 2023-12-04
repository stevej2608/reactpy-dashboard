from typing import List, Any, Optional
from pydantic import BaseModel
from .types import Options, ReactpyTableBase, AbstractPaginator, AbstractRowModel



class RowModel(BaseModel):
    rows: List[Any] = []


class ReactpyTable(ReactpyTableBase):

    table_data: List[Any] = []
    columns: None

    paginator: Optional[AbstractPaginator] = None
    row_model: Optional[AbstractRowModel] = None

    def __init__(self, table_data: List[Any]):
        self.table_data = table_data if table_data else []


    def get_row_model(self):
        row_model = RowModel(rows=self.table_data[0:10])
        return row_model


def use_reactpy_table(options: Options = Options()) -> ReactpyTable:

    table = ReactpyTable(options.data)
    for plugin_factory in options.plugins:
        name, plugin = plugin_factory(table)
        setattr(table, name, plugin)

    return table
