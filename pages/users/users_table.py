from typing import List
from reactpy import component, html, use_memo, use_state
from utils.child_list import ChildList
from utils.logger import log
from reactpy_table import use_reactpy_table, Options, Columns, Column, SimplePaginator, SimpleRowModel

from ..components.table_paginator import TablePaginator
from ..components.table_widgets import Table, TBody, THead, TRow, Checkbox, RowCheckbox, Text, EditButtons, ColumnHeader

from .user_data import make_users, User

COLS: Columns = [
    Column(name='index', label='#'),
    Column(name='name', label='Name', width="w-80"),
    Column(name='position', label='Position', width="w-48"),
    Column(name='company', label='Company', width="w-48"),
    Column(name='status', label='Status', width="w-48")
    ]

@component
def UsersTable():

    all_checked, set_all_checked = use_state(False)

    @component
    def TableHead(columns: Columns):

        cols = [ColumnHeader(width=col.width, title=col.label) for col in columns[1:5]]

        return THead(
            html.tr(
                Checkbox("checkbox-all", checked=all_checked, on_click=lambda event: set_all_checked(not all_checked)),
                ChildList(*cols),
                html.th({'scope': 'col', 'class_name': 'p-4'})
            )
        )

    @component
    def TableRow(index, row: User):

        checked, set_checked = use_state(all_checked)


        @component
        def NameAndPicture(row: User, width=""):
            return html.td({'class_name': 'p-4 flex items-center whitespace-nowrap space-x-6 mr-12 lg:mr-0'},
                html.img({'class_name': 'h-10 w-10 rounded-full', 'src': row.img, 'alt': f'{row.name} avatar'}),
                html.div({'class_name': 'text-sm font-normal text-gray-500'},
                    html.div({'class_name': 'text-base font-semibold text-gray-900'}, row.name),
                    html.div({'class_name': 'text-sm font-normal text-gray-500'}, row.email)
                )
            )


        return TRow(
            RowCheckbox(checked=checked, on_click=lambda event: set_checked(not checked)),
            NameAndPicture(row),
            Text(value=row.position),
            Text(value=row.country),
            Text(value=row.status),
            EditButtons(label='user')
        )


    @component
    def TableBody(table: List[User]):
        table_rows = [TableRow(index, row) for index, row in enumerate(table)]
        return TBody(ChildList(*table_rows))


    log.info('ProductsTable')

    # https://reactpy.dev/docs/reference/hooks-api.html

    table_data = use_memo(lambda: make_users(1000))

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
