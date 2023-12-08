from abc import abstractmethod
from .abstract_plugin import Plugin
from .table_data import Column

class ColumnSort(Plugin):

    @abstractmethod
    def toggle_sort(self, col:Column) -> bool: ...

    @abstractmethod
    def is_sort_reverse(self, col:Column) -> bool: ...
