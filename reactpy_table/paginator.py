
import math
from utils.logger import log
from .types import Paginator, Table


# packages/table-core/src/features/Pagination.ts#L157

DEFAULT_PAGE_SIZE = 10


class SimplePaginator(Paginator):

    @staticmethod
    def init(table: Table) -> None:
        table.paginator = SimplePaginator(table=table.data, page_size=DEFAULT_PAGE_SIZE)

    @property
    def page_count(self) -> int:
        row_count = len(self.table.rows)
        return math.ceil(row_count / self.page_size)


    def first_page(self):
        log.info('firsts_page')


    def previous_page(self):
        log.info('previous_page')


    def next_page(self):
        log.info('next_page')
        self.set_page_index(self.page_index + 1)


    def last_page(self):
        log.info('last_page')


    def set_page(self, page:int):
        log.info('set_page')


    def set_page_size(self, page:int):
        log.info('set_page_size')


    def set_page_index(self, page_index:int):
        log.info('set_page_index')
        self.page_index = page_index


    # ./tmp/table/packages/table-core/src/features/Pagination.ts#L299

    def get_can_previous_page(self):
        return self.page_index > 0

    # ./tmp/table/packages/table-core/src/features/Pagination.ts#L301

    def get_can_next_page(self):
        page_count = self.page_count

        if page_count == -1:
            return True

        if page_count == 0:
            return False

        return self.page_index < page_count - 1


    # ./tmp/table/packages/table-core/src/features/Pagination.ts#L344

