from typing import Callable, Any, Union
from reactpy import use_state
from utils.logger import log

from .types import TableData
from .abstract_table import Table, Options

class ReactpyTable(Table):
    ...


def use_reactpy_table(options: Options = Options()) -> ReactpyTable:

    set_table: Union[Callable[[Union[Any, Callable[[Any], Any]]], None], None]  = None

    def _create_table() -> ReactpyTable:
        table_data = TableData(rows=options.data)
        table = ReactpyTable(data=table_data)

        def _updater():
            new = table.copy()
            try:
                set_table(new)
            except Exception as ex:
                log.info('Update model failed %s', ex)

        for plugin_factory in options.plugins:
            plugin_factory(table, _updater)

        return table

    table, set_table = use_state(_create_table)

    log.info('use_reactpy_table')

    return table
