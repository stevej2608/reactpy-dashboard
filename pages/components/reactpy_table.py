
from typing import List, Any
from pydantic import BaseModel
from reactpy import event

from utils.logger import log

# https://solidjs-table.vercel.app/


class Pagination(BaseModel):
    page_index: int = 0


class TableState(BaseModel):
    pagination : Pagination = None

class RowModel(BaseModel):
    rows: List[Any] = None

class ReactPyTable:

    def __init__(self, table):
        self.table = table
        self.state = TableState(pagination=Pagination())


    @event
    def previous_page(self):
        log.info('previous_page')

    @event
    def next_page(self):
        log.info('next_page')


    def get_can_previous_page(self):
        return True

    def get_can_next_page(self):
        return True


    def get_state(self):
        return self.state


    def get_page_count(self) -> int:
        return 99


    def get_row_model(self):
        row_model = RowModel(rows=self.table[0:10])
        return row_model


class ColumnDef:
   pass

def get_core_row_model():
    pass

def get_pagination_row_model():
    pass

def create_reactpy_table(table_data: List[Any], columns: List[dict], pagination_model, row_model):
    return ReactPyTable(table_data)
