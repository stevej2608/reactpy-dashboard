
from utils.logger import log

from .table_data import RowData, Column
from .abstract_plugin import Updater, update_state
from .abstract_table import Table
from .abstract_table import TableSearch



class SimpleTableSearch(TableSearch):

    initial_values: RowData


    @staticmethod
    def init(table: Table, updater: Updater) -> None:

        table.search = SimpleTableSearch(
            data=table.data,
            initial_values = table.data.rows,
            updater=updater
            )


    @update_state
    def table_search(self, text:str):

        def _filter(element: Column):
            element_text = ' '.join([str(val)  for val in element.dict().values()])
            return text in element_text

        result = filter(_filter, self.initial_values)
        self.data.rows = list(result)
