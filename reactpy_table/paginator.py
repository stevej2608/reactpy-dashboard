
from typing import List, Any
from functools import wraps
import math
from utils.logger import log
from .types import Paginator, Table, Updater


def set_state(method):
    @wraps(method)
    def _impl(self: Paginator, *args, **kwargs):
        old = self.copy()
        result = method(self, *args, **kwargs)
        new = self.copy()
        if old != new:
            log.info('Update the model!!!')
            self.updater(old, new)
        return result
    return _impl


DEFAULT_PAGE_SIZE = 10


class SimplePaginator(Paginator):

    @staticmethod
    def init(table: Table, updater: Updater) -> None:
        table.paginator = SimplePaginator(
            table=table.data, 
            page_size=DEFAULT_PAGE_SIZE,
            updater = updater
            )

    @property
    def rows(self) -> List[Any]:
        low = self.page_size * self.page_index
        high = min(low + self.page_size, len(self.table.rows))
        return self.table.rows[low:high]


    @property
    def page_count(self) -> int:
        row_count = len(self.table.rows)
        return math.ceil(row_count / self.page_size)


    def first_page(self):
        log.info('firsts_page')
        self.set_page(0)


    def previous_page(self):
        log.info('previous_page')
        self.set_page_index(self.page_index - 1)


    def next_page(self):
        log.info('next_page')
        self.set_page_index(self.page_index + 1)


    def last_page(self):
        log.info('last_page')
        last_page = self.page_count() - 1
        self.set_page_index(last_page)


    def set_page_size(self, page:int):
        log.info('set_page_size')


    @set_state
    def set_page_index(self, page_index:int):
        log.info('set_page_index')
        self.page_index = page_index


    def get_can_previous_page(self) -> bool:
        return self.page_index > 0


    def get_can_next_page(self) -> bool:
        page_count = self.page_count

        if page_count == -1:
            return True

        if page_count == 0:
            return False

        return self.page_index < page_count - 1
