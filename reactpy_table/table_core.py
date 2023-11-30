from typing import List, Any
from pydantic import BaseModel
from .types import Options

class RowModel(BaseModel):
    rows: List[Any] = None


class ReactpyTable:

    def __init__(self, table_data: Any):
        self.table_data = table_data


    def get_row_model(self):
        row_model = RowModel(rows=self.table_data[0:10])
        return row_model


def use_reactpy_table(options: Options=None) -> ReactpyTable:
    table = ReactpyTable(options.data)
    for plugin_factory in options.plugins:
        name, plugin = plugin_factory(table)
        setattr(table, name, plugin)

    return table
