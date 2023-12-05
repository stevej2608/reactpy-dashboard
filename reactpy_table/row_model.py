from .types import  AbstractRowModel, AbstractTable


class RowModel(AbstractRowModel):

    def __init__(self, table: AbstractTable):
        self.table = table


    @staticmethod
    def get_core_row_model(table: AbstractTable) -> [str, AbstractRowModel]:
        return ['row_model', RowModel(table)]
