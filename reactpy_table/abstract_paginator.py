from abc import abstractmethod
from .abstract_plugin import Plugin


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
