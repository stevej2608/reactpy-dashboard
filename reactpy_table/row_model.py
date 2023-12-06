from .types import  RowModel, Table, Updater


class SimpleRowModel(RowModel):


    @staticmethod
    def init(table: Table, updater: Updater) -> None:
        table.row_model = SimpleRowModel(
            table=table.data, 
            updater = updater
            )
