from .types import ReactpyTable
from .plugin import Plugin


class RowModel(Plugin):

    @staticmethod
    def get_core_row_model(table: ReactpyTable) -> [str, Plugin]:
        return ['row_model', RowModel(table)]
