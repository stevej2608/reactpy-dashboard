from abc import abstractmethod
from functools import wraps
from .types import Plugin


class Paginator(Plugin):

    page_index: int = 0
    page_size: int

    @property
    @abstractmethod
    def rows(self): ...

    @property
    @abstractmethod
    def page_count(self): ...

    @abstractmethod
    def first_page(self): ...

    @abstractmethod
    def previous_page(self): ...

    @abstractmethod
    def next_page(self): ...

    @abstractmethod
    def last_page(self): ...

    @abstractmethod
    def get_can_previous_page(self) -> bool: ...

    @abstractmethod
    def get_can_next_page(self) -> bool: ...


def set_state(method):
    @wraps(method)
    def _impl(self: Paginator, *args, **kwargs):
        old = self.copy()
        result = method(self, *args, **kwargs)
        new = self.copy()
        if old != new:
            self.updater()
        return result
    return _impl
