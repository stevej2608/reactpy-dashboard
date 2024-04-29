from reactpy import component, html, use_memo, use_state
from reactpy.core.types import VdomDict

from reactpy_table import ColumnDef, Columns, ITableSearch, Table, Options, use_reactpy_table, FeatureControl

from utils.child_list import ChildList
from utils.component_class import ComponentClass, class_component
from utils.logger import log

from ..components.table_paginator import TablePaginator
from ..components.table_widgets import Checkbox, ColumnHeader, EditButtons, RowCheckbox, TTable, TBody, Text, THead, TRow
from .user_data import User, make_users

COLS: Columns = [
    ColumnDef(name='index', label='#'),
    ColumnDef(name='name', label='Name', width="w-80"),
    ColumnDef(name='position', label='Position', width="w-48"),
    ColumnDef(name='company', label='Company', width="w-48"),
    ColumnDef(name='status', label='Status', width="w-48")
    ]

@class_component
class UsersTable(ComponentClass):

    @property
    def search(self) -> ITableSearch[User]:
        return self.table.search

    def __init__(self):
        super().__init__()

        # https://reactpy.dev/docs/reference/hooks-api.html

        table_data = use_memo(lambda: make_users(1000))

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
                    ChildList(*cols),
                    html.th({'scope': 'col', 'class_name': 'p-4'})
                )
            )

        @component
        def TableRow(index:int, row: User):

            checked, set_checked = use_state(all_checked)


            @component
            def NameAndPicture(row: User, width:str=""):
                return html.td({'class_name': 'p-4 flex items-center whitespace-nowrap space-x-6 mr-12 lg:mr-0'},
                    html.img({'class_name': 'h-10 w-10 rounded-full', 'src': row.img, 'alt': f'{row.name} avatar'}),
                    html.div({'class_name': 'text-sm font-normal text-gray-500'},
                        html.div({'class_name': 'text-base font-semibold text-gray-900'}, row.name),
                        html.div({'class_name': 'text-sm font-normal text-gray-500'}, row.email)
                    )
                )


            return TRow(
                RowCheckbox(checked=checked, on_click=lambda: set_checked(not checked)),
                NameAndPicture(row),
                Text(value=row.position),
                Text(value=row.country),
                Text(value=row.status),
                EditButtons(label='user')
            )


        @component
        def TableBody(table: Table[User]):
            rows = table.data.rows
            table_rows = [TableRow(index, row) for index, row in enumerate(rows)]
            return TBody(ChildList(*table_rows))


        log.info('Users Table')

        return html._(
            TTable(
                TableHead(COLS),
                TableBody(self.table)
            ),
            TablePaginator(self.table.paginator)
        )
