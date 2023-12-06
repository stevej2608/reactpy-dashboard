from typing import List, Callable, Any
from functools import wraps
from pydantic import BaseModel
from .types import TableData


Updater = Callable[[], None]

class Plugin(BaseModel):
    table: TableData
    updater: Updater


def set_state(method):
    @wraps(method)
    def _impl(self: Plugin, *args, **kwargs):
        old = self.copy()
        result = method(self, *args, **kwargs)
        new = self.copy()
        if old != new:
            self.updater()
        return result
    return _impl
