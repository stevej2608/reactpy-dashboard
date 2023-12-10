from typing import Dict, Any
from pydantic import BaseModel

from .abstract_plugin import Updater, update_state
from .abstract_column_sort import ColumnSort
from .table_data import Column
from .abstract_table import Table

class ColumnState(BaseModel):
    reverse: bool = False


class SimpleColumnSort(ColumnSort):

    state: Dict[str, ColumnState]


    @staticmethod
    def init(table: Table, updater: Updater) -> None:


        state = {}
        for col in table.data.cols:
            name = col if isinstance(col, str) else col.name
            state[name] = ColumnState()

        table.sort = SimpleColumnSort(
            data=table.data,
            state = state,
            updater=updater
            )

    @update_state
    def toggle_sort(self, col:Column) -> bool:

        def _sort(col:Column, element: Any):
            name = col if isinstance(col, str) else col.name
            return getattr(element, name)
   
        state = self.get_state(col)
        state.reverse = not state.reverse

        self.data.rows.sort(key=lambda element: _sort(col, element), reverse=state.reverse)

        return state.reverse


    def is_sort_reverse(self, col:Column)-> bool:
        state = self.get_state(col)
        return state.reverse


    def get_state(self, col:Column):
        return self.state[col.name]
