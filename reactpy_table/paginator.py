
from pydantic import BaseModel
from utils.logger import log
from .types import ReactpyTable
from .plugin import Plugin


class TableState(BaseModel):
    page_page_size: int = 10
    page_index: int = 0
    page_count: int = 0


class Paginator(Plugin):

    def __init__(self, table):
        super().__init__(table)
        self.table = table
        self.state = TableState()


    @staticmethod
    def get_pagination_row_model(table: ReactpyTable) -> [str, Plugin]:
        return ['paginator', Paginator(table)]


    def first_page(self):
        log.info('firsts_page')


    def previous_page(self):
        log.info('previous_page')


    def next_page(self):
        log.info('next_page')


    def last_page(self):
        log.info('last_page')


    def set_page(self, page:int):
        log.info('set_page')


    def set_page_size(self, page:int):
        log.info('set_page_size')


    # ./tmp/table/packages/table-core/src/features/Pagination.ts

    def get_can_previous_page(self):
        return self.get_state().pagination.page_index > 0


    def get_can_next_page(self):
        page_index = self.get_state().pagination.page_index
        page_count = self.get_page_count()

        if page_count == -1:
            return True

        if page_count == 0:  
            return False

        return page_index < page_count - 1


    def get_state(self) -> TableState:
        return self.state


    def get_page_count(self) -> int:
        return 99