from .types import ReactpyTable
from typing import List, Callable, Any, Tuple


class Plugin:

    def __init__(self, table: ReactpyTable):
        self.table = table
