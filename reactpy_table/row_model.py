from .types import  AbstractRowModel
from .table_core import ReactpyTable

class RowModel(AbstractRowModel):

    def __init__(self, table: ReactpyTable):
        self.table = table


    @staticmethod
    def get_core_row_model(table: ReactpyTable) -> [str, AbstractRowModel]:
        return ['row_model', RowModel(table)]
