from typing import List, Callable
from reactpy import component, html, use_memo, use_state
from utils.child_list import ChildList
from utils.logger import log
from reactpy_table import use_reactpy_table, Options, Columns, Column, SimplePaginator, SimpleRowModel

from ..components.table_paginator import TablePaginator
from ..components.table_widgets import Table, TBody, THead, TRow, Checkbox, Text, EditButtons, ColumnHeader

from .products_data import make_products, Product

COLS: Columns = [
    Column(name='index', label='#'),
    Column(name='name', label='Product Name'),
    Column(name='description', label='Description'),
    Column(name='technology', label='Technology'),
    Column(name='id', label='ID'),
    Column(name='price', label='Price')
    ]

@component
def ProductsTable():

    all_checked, set_all_checked = use_state(False)

    @component
    def TableHead(columns: Columns):
        return THead(
            html.tr(
                Checkbox(checked=all_checked, on_click=lambda event: set_all_checked(not all_checked)),
                [ColumnHeader(width="200px", title=col.label) for col in columns[1:5]],
                html.th({'scope': 'col', 'class_name': 'p-4'})
            )
        )

    @component
    def TableRow(index, row: Product):

        checked, set_checked = use_state(all_checked)

        @component
        def Name(name:str):
            return html.td({'class_name': 'whitespace-nowrap p-4 text-sm font-normal text-gray-500'},
                html.div({'class_name': 'text-base font-semibold text-gray-900'}, name),
                html.div({'class_name': 'text-sm font-normal text-gray-500'}, "Html templates")
            )


        return TRow(
            Checkbox(checked=checked, on_click=lambda event: set_checked(not checked)),
            Name(row.name),
            Text(value=row.technology),
            Text(value=row.id),
            Text(value=row.price),
            EditButtons()
        )


    @component
    def TableBody(table: List[Product]):
        table_rows = [TableRow(index, row) for index, row in enumerate(table)]
        return TBody(ChildList(*table_rows))


    log.info('ProductsTable')

    # https://reactpy.dev/docs/reference/hooks-api.html

    table_data = use_memo(lambda: make_products(10000))

    table = use_reactpy_table(Options(
        rows=table_data,
        cols=COLS,
        plugins=[
            SimplePaginator.init,
            SimpleRowModel.init
            ]
        ))


    return html._(
        Table(
            TableHead(COLS),
            TableBody(table.paginator.rows)
        ),
        TablePaginator(table.paginator)
    )
