from typing import Dict
from pydantic import BaseModel

from utils.logger import log

from .abstract_plugin import Updater
from .abstract_table import Table
from .abstract_table import TableSearch



class SimpleTableSearch(TableSearch):


    @staticmethod
    def init(table: Table, updater: Updater) -> None:

        table.search = SimpleTableSearch(
            data=table.data,
            updater=updater
            )


    def table_search(self, text:str):
        log.info('search %s', text)
