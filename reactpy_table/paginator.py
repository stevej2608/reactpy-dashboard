
import math
from pydantic import BaseModel
from utils.logger import log
from .types import AbstractPaginator, AbstractPlugin, AbstractTable


# packages/table-core/src/features/Pagination.ts#L157

class PaginationState(BaseModel):
    page_size: int = 10
    page_index: int = 0
    # page_count: int = 0


class Paginator(AbstractPaginator):

    def __init__(self, table: AbstractTable):
        self.table = table
        self.state = PaginationState()


    @staticmethod
    def get_pagination_row_model(table: AbstractTable) -> [str, AbstractPlugin]:
        return ['paginator', Paginator(table)]


    def first_page(self):
        log.info('firsts_page')


    def previous_page(self):
        log.info('previous_page')


    def next_page(self):
        log.info('next_page')
        page_index = self.get_state().page_index
        self.set_page_index(page_index + 1)


    def last_page(self):
        log.info('last_page')


    def set_page(self, page:int):
        log.info('set_page')


    def set_page_size(self, page:int):
        log.info('set_page_size')


    def set_page_index(self, page_index:int):
        log.info('set_page_index')
        self.state = self.state.copy(update={'page_index': page_index})
        self.table.set_table()

    # ./tmp/table/packages/table-core/src/features/Pagination.ts#L299

    def get_can_previous_page(self):
        return self.get_state().page_index > 0

    # ./tmp/table/packages/table-core/src/features/Pagination.ts#L301

    def get_can_next_page(self):
        page_index = self.get_state().page_index
        page_count = self.get_page_count()

        if page_count == -1:
            return True

        if page_count == 0:
            return False

        return page_index < page_count - 1


    def get_state(self) -> PaginationState:
        return self.state

    # ./tmp/table/packages/table-core/src/features/Pagination.ts#L344

    def get_page_count(self) -> int:
        page_size = self.get_state().page_size
        row_count = len(self.table.table_data)
        return math.ceil(row_count / page_size)
