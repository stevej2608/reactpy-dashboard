from .types import AbstractPlugin
from .table_core import ReactpyTable

class Plugin(AbstractPlugin):

    def __init__(self, table: ReactpyTable):
        self.table = table
