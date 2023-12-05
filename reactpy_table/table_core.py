from typing import List, Any, Optional
from pydantic import BaseModel
from reactpy import use_state
from utils.logger import log
from .types import Options, AbstractTable, AbstractPaginator, AbstractRowModel, TableData



class RowModel(BaseModel):
    rows: List[Any] = []


class ReactpyTable(AbstractTable):

    @property
    def table_data(self) -> TableData:
        return self._table_data

    @property
    def paginator(self) -> Optional[AbstractPaginator]:
        return self._paginator

    @property
    def row_model(self) -> Optional[AbstractRowModel]:
        return self._row_model

    def __init__(self, table_data: List[Any]):
        self._table_data = table_data if table_data else []
        self._paginator = None
        self._row_model = None
        self._updater = None


    def set_table(self, table: Optional[AbstractTable] = None):
        table = table if table else self
        if self._updater:
            self._updater(table)


    def set_updater(self, updater):
        self._updater = updater


    def get_row_model(self):
        row_model = RowModel(rows=self.table_data[0:10])
        return row_model


def use_reactpy_table(options: Options = Options()) -> ReactpyTable:

    def _create_table():
        table = ReactpyTable(options.data)
        for plugin_factory in options.plugins:
            name, plugin = plugin_factory(table)
            setattr(table, f"_{name}", plugin)
        return table
    
    log.info('use_reactpy_table')

    table, set_table = use_state(_create_table())

    log.info('use_reactpy_table2')

    table.set_updater(set_table)

    return table
