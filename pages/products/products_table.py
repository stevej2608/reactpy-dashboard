
from reactpy import component, html, use_memo, use_state
from reactpy.core.types import VdomDict

from reactpy_table import ColumnDef, Columns, ITableSearch, Table, Options, use_reactpy_table, FeatureControl

from utils.component_class import ComponentClass, class_component
from utils.logger import log

from ..components.table_paginator import TablePaginator
from ..components.table_widgets import Checkbox, ColumnHeader, EditButtons, RowCheckbox, TTable, TBody, Text, THead, TRow
from .products_data import Product, make_products

COLS: Columns = [
    ColumnDef(name='index', label='#'),
    ColumnDef(name='name', label='Product Name', width="w-80"),
    ColumnDef(name='technology', label='Technology', width="w-48"),
    ColumnDef(name='id', label='ID', width="w-48"),
    ColumnDef(name='price', label='Price', width="w-48")
    ]

@class_component
class ProductsTable(ComponentClass):

    @property
    def search(self) -> ITableSearch[Product]:
        return self.table.search

    def __init__(self):
        super().__init__()

        # https://reactpy.dev/docs/reference/hooks-api.html

        table_data = use_memo(lambda: make_products(10000))

        self.table = use_reactpy_table(Options(
            rows=table_data,
            cols=COLS,
            pagination_control=FeatureControl.DEFAULT
            ))

    def render(self) -> VdomDict:

        all_checked, set_all_checked = use_state(False)

        @component
        def TableHead(columns: Columns):

            cols = [ColumnHeader(width=col.width, title=col.label) for col in columns[1:5]]

            return THead(
                html.tr(
                    Checkbox("checkbox-all", checked=all_checked, on_click=lambda: set_all_checked(not all_checked)),
                    *cols,
                    html.th({'scope': 'col', 'class_name': 'p-4'})
                )
            )

        @component
        def TableRow(index:int, row: Product):

            checked, set_checked = use_state(all_checked)

            @component
            def Name(name:str, width:str=""):
                return html.td({'class_name': f'whitespace-nowrap {width} p-4 text-sm font-normal text-gray-500'},
                    html.div({'class_name': 'text-base font-semibold text-gray-900'}, name),
                    html.div({'class_name': 'text-sm font-normal text-gray-500'}, "Html templates")
                )


            return TRow(
                RowCheckbox(checked=checked, on_click=lambda: set_checked(not checked)),
                Name(row.name),
                Text(value=row.technology),
                Text(value=row.id,),
                Text(value=row.price),
                EditButtons(label='item')
            )


        @component
        def TableBody(table: Table[Product]):
            rows = table.data.rows
            table_rows = [TableRow(index, row) for index, row in enumerate(rows)]
            return TBody(*table_rows)

        log.info('Products Table')

        return html._(
            TTable(
                TableHead(COLS),
                TableBody(self.table)
            ),
            TablePaginator(self.table.paginator)
        )
