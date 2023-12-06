from typing import Optional
from reactpy import use_state
from utils.logger import log
from .types import Options, Table, TableData, RowModel



class ReactpyTable(Table):


    def set_table(self, table: Optional[Table] = None):
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
        table_data = TableData(rows=options.data)
        table = ReactpyTable(data=table_data)
        for plugin_factory in options.plugins:
            plugin_factory(table)

        return table

    table, set_table = use_state(_create_table)

    log.info('use_reactpy_table')

    # table.set_updater(set_table)

    return table
