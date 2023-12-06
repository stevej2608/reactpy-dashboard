from .types import  RowModel, Updater

from .abstract_table import Table

class SimpleRowModel(RowModel):

    @staticmethod
    def init(table: Table, updater: Updater) -> None:
        table.row_model = SimpleRowModel(
            table=table.data, 
            updater = updater
            )
