from typing import List
from reactpy import component, html, use_memo
from utils.child_list import ChildList
from utils.logger import log
from reactpy_table import use_reactpy_table, Options, SimplePaginator, SimpleRowModel

from ..components.table_paginator import TablePaginator
from ..components.table_widgets import Table, TBody, THead, TRow, Checkbox, Text, EditButtons, ColumnHeader

from .products_data import make_products, Product

columns = [
    {
        "accessor_key": "name",
        "header": "Product Name "
    },
    {
        "accessor_key": "technology",
        "header": " Technology "
    },
    {
        "accessor_key": "id",  
        "header": "ID"
    },
    {
        "accessor_key": "price",
        "header": "Price"
    }
]

COLS = ['#', 'Name', 'Description', 'Technology', 'ID', 'Price']


@component
def TableHead(columns = None):
    return THead(
        html.tr(
            Checkbox(),
            ColumnHeader(width="200px", title="Product Name"),
            ColumnHeader(width="200px", title="Technology"),
            ColumnHeader(width="200px", title="ID"),
            ColumnHeader(width="200px", title="Price"),
            html.th({'scope': 'col', 'class_name': 'p-4'})
        )
    )

@component
def TableRow(index, row: Product):

    @component
    def Name(name:str):
        return html.td({'class_name': 'whitespace-nowrap p-4 text-sm font-normal text-gray-500'},
            html.div({'class_name': 'text-base font-semibold text-gray-900'}, name),
            html.div({'class_name': 'text-sm font-normal text-gray-500'}, "Html templates")
        )


    return TRow(
        Checkbox(),
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

@component
def ProductsTable():

    log.info('ProductsTable')

    # https://reactpy.dev/docs/reference/hooks-api.html

    table_data = use_memo(lambda: make_products(10000))

    table = use_reactpy_table(Options(
        data=table_data,
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
