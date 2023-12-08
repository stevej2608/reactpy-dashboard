from abc import abstractmethod
from .abstract_plugin import Plugin


class TableSearch(Plugin):

    @abstractmethod
    def table_search(self, text:str): ...
