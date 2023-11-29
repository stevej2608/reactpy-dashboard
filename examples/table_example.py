from typing import List, Dict
from pydantic import BaseModel
from reactpy import component, html, use_state, event
from utils.logger import log, logging
from utils.make_data import make_data
from examples.pico_run import pico_run
from pages.components.reactpy_table import get_core_row_model, get_pagination_row_model, ColumnDef, create_reactpy_table, ReactPyTable

from modules.reactpy_helpers import For

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

COLS = ['#', 'Name', 'Description', 'Technology', 'ID', 'Price']

class Product(BaseModel):
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
def TablePaginator(table: ReactPyTable):

    @component
    def Button(text:str, action):

        @event
        def onclick(event):
            action()

        return html.button({'onclick': onclick}, text)

    @component
    def PageSize(size:int):

        @event
        def onclick(event):
            table.set_page_size(size)

        return html.option({'value': size, 'onclick': onclick}, f"Show {size}")


    @component
    def PageSizeSelect(sizes:List[int]):

        @event
        def on_change(event):
            table.set_page_size(event['currentTarget']['value'])

        @component
        def PageOption(size:int):
            return html.option({'value': size}, f"Show {size}")

        return html.select({'value': sizes[0], "on_change": on_change}, For(PageOption, sizes))


    @component
    def PageInput():

        @event
        def on_change(event):
            table.set_page(event['currentTarget']['value'])

        return html._(
            Text("Go to page:"),
            html.input({'type': 'number', 'value': 1, "on_change": on_change}),
        )

    return html.div({'class_name': 'grid', 'style': {'align-items': 'center','grid-template-columns': '2.5fr 1.5fr 1.5fr 2.5fr 4fr 1.2fr 2fr 3fr'}},
        Button("<<", table.first_page),
        Button("<", table.previous_page),
        Button(">", table.next_page),
        Button(">>", table.last_page),
        Text("Page",html.strong("1 of 10")),
        PageInput(),
        PageSizeSelect([10, 20, 30, 40, 50])
    )


@component
def Text(*children):
    """Add the pico button margin to make the 
    given text line up with the button text."""

    return html.span({'style': 'margin-bottom: var(--spacing);'}, *children)


@component
def THead(columns: List[str]):
    return html.thead(
        For(html.th, iterator=columns)
    )


def TRow(index: int, row: Product):
    return  html.tr(
        html.th(index),
        html.td(row.name),
        html.td(row.description),
        html.td(row.technology),
        html.td(row.id),
        html.td(row.price)
    )


def TBody(table: ReactPyTable):
    return  html.tbody(
        For(TRow, iterator=enumerate(table.get_row_model().rows))
    )

@component
def TFoot(columns: List[str]):
    return html.tfoot(
        For(html.td, columns)
    )

@component
def AppMain():


    table_data, set_table_data = use_state(make_products(999))

    table = create_reactpy_table(table_data, COLS, get_core_row_model(), get_pagination_row_model())


    return html.div(
        html.table({"role": "grid"},
            THead(COLS),
            TBody(table),
            TFoot(COLS),
        ),
        TablePaginator(table)
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(AppMain)
