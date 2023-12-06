from .types import  RowModel, Table


class SimpleRowModel(RowModel):


    @staticmethod
    def init(table: Table) -> None:
        table.row_model = SimpleRowModel(table=table.data)
