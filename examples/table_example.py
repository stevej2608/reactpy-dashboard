from typing import List, Callable

from pydantic import BaseModel
from reactpy import component, event, html, use_memo, use_state
from reactpy.core.component import Component

from reactpy_table import ColumnDef,Columns,IPaginator,Options,Table,use_reactpy_table, ITableSearch


from utils.logger import log, logging
from utils.make_data import make_data
from utils.pico_run import pico_run
from utils.reactpy_helpers import For
from utils.types import EventArgs

# https://codesandbox.io/p/devbox/tanstack-table-example-expanding-jr4nn3?embed=1



PRODUCTS = [
    {"name": "Education Dashboard", "description": "Html templates", "technology": "Angular", "id": "#194556", "price": "$149"},
    {"name": "React UI Kit", "description": "Html templates", "technology": "React JS", "id": "#623232", "price": "$129"},
    {"name": "DashboardPro", "description": "Html templates", "technology": "SolidJS", "id": "#194334", "price": "$449"},
    {"name": "Charts Package", "description": "Fancy charts", "technology": "Angular", "id": "#323323", "price": "$129"},
    {"name": "Server Render", "description": "NodeJS", "technology": "Typescript", "id": "#994336", "price": "$749"},
    {"name": "Accounts Package", "description": "NodeJS", "technology": "Typescript", "id": "#144256", "price": "$779"},
    {"name": "Grav CMS", "description": "Content Management", "technology": "PHP", "id": "#624478", "price": "$29"},
    {"name": "Wordpress", "description": "Content Management", "technology": "PHP", "id": "#192656", "price": "$55"}
]

COLS: Columns = [
    ColumnDef(name='index', label='#'),
    ColumnDef(name='name', label='Name'),
    ColumnDef(name='description', label='Description'),
    ColumnDef(name='technology', label='Technology'),
    ColumnDef(name='id', label='ID'),
    ColumnDef(name='price', label='Price')
    ]


class Product(BaseModel):
    index: int
    name: str
    description: str
    technology: str
    id: str
    price: str


def make_products(number: int) -> List[Product] :
    return make_data(number, PRODUCTS, Product)

# https://medium.com/@jordammendes/build-powerfull-tables-in-reactjs-with-tanstack-9d57a3a63e35
# https://tanstack.com/table/v8/docs/examples/react/expanding



@component
def TablePaginator(paginator: IPaginator[Product]):

    @component
    def Button(text:str, action:Callable[...,None], disabled:bool=False):

        @event
        def onclick(event: EventArgs):
            action()

        return html.button({'onclick': onclick, 'disabled': disabled}, text)


    @component
    def PageSizeSelect(sizes:List[int]):

        @event
        def on_change(event: EventArgs):
            page_size = int(event['currentTarget']['value'])
            paginator.set_page_size(page_size)


        def PageOption(size:int):
            return html.option({'value': size}, f"Show {size}")

        return html.select({'value': sizes[0], "on_change": on_change}, For(PageOption, sizes))


    @component
    def PageInput():

        count_value, set_count = use_state(0)

        @event(prevent_default=True)
        def on_change(event: EventArgs):

            try:
                new_value = int(event['currentTarget']['value'])
                new_value = max(new_value, 1)
                new_value = min(new_value, paginator.page_count)
            except Exception:
                new_value = 1

            log.info('new_value = %d', new_value)

            if paginator.page_index != new_value - 1:
                paginator.set_page_index(new_value - 1)
            else:
                set_count(count_value + 1)

        log.info('render new_value = %d', paginator.page_index + 1)

        return html._(
            Text("Go to page:"),
            html.input({'type': 'number', 'value': paginator.page_index + 1, "on_change": on_change}),
        )

    no_previous = not paginator.can_get_previous_page()
    no_next = not paginator.can_get_next_page()

    return html.div({'class_name': 'grid', 'style': {'align-items': 'center','grid-template-columns': '2.5fr 1.5fr 1.5fr 2.5fr 4fr 1.2fr 2fr 3fr'}},
        Button("<<", paginator.first_page, disabled = no_previous),
        Button("<", paginator.previous_page, disabled = no_previous),
        Button(">", paginator.next_page, disabled = no_next),
        Button(">>", paginator.last_page, disabled = no_next),
        Text("Page",html.strong(f" {paginator.page_index + 1} of {paginator.page_count}")),
        PageInput(),
        PageSizeSelect([10, 20, 30, 40, 50])
    )


@component
def Text(*children: List[Component]):
    """Add the pico button margin to make the 
    given text line up with the button text."""

    return html.span({'style': 'margin-bottom: var(--spacing);'}, *children)


@component
def Search(search: ITableSearch[Product]):

    @event
    def on_change(event: EventArgs):
        text = event['currentTarget']['value']
        search.table_search(text)

    return html.input({'type': 'search', 'placeholder': 'Search', 'aria-label': 'Search', 'onchange': on_change})

@component
def THead(table: Table[Product]):


    def text_with_arrow(col: ColumnDef):


        @event
        def on_click(event: EventArgs):
            log.info('onclick col=%s', col)
            table.sort.toggle_sort(col)

        # https://symbl.cc/en/collections/arrow-symbols/

        up = table.sort.is_sort_reverse(col)

        text = col.label + (" 🠕" if up else " 🠗")
        return html.th({'onclick': on_click}, text)

    columns = table.data.cols

    return html.thead(
        For(text_with_arrow, iterator=columns)
    )


@component
def TColgroup(col_widths: List[int]):
    """Return a html.colgroup with the given widths"""
    return  html.colgroup(
        [html.col({'style': {'width':f"{width}px"}}) for width in col_widths]
    )


def TRow(index: int, row: Product):
    return  html.tr(
        html.td(str(row.index)),
        html.td(row.name),
        html.td(row.description),
        html.td(row.technology),
        html.td(row.id),
        html.td(row.price),
    )


def TBody(table: List[Product]):
    return  html.tbody(
        For(TRow, iterator=enumerate(table))
    )


@component
def TFoot(columns: Columns):
    return html.tfoot(
        For(html.td, [col.label for col in columns])
    )


@component
def AppMain():

    table_data = use_memo(lambda: make_products(9999))

    table = use_reactpy_table(Options(
        rows=table_data,
        cols = COLS,
    ))


    return html.div(
        html.br(),
        html.h2('ReactPy Table Example'),
        Search(table.search),
        html.table({"role": "grid"},
            TColgroup([80, 150, 100, 100, 100, 100]),
            THead(table),
            TBody(table.paginator.rows),
            TFoot(table.data.cols),
        ),
        TablePaginator(table.paginator)
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(AppMain)
