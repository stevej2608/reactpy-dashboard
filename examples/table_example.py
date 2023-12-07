from typing import List
from pydantic import BaseModel
from reactpy import component, html, use_state, use_memo, event
from utils.logger import log, logging
from utils.make_data import make_data
from examples.pico_run import pico_run

from reactpy_table import use_reactpy_table, Options, Paginator, SimplePaginator


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
def TablePaginator(paginator: Paginator):

    @component
    def Button(text:str, action, disabled=False):

        @event
        def onclick(event):
            action()

        return html.button({'onclick': onclick, 'disabled': disabled}, text)

    @component
    def PageSize(size:int):

        @event
        def onclick(event):
            paginator.set_page_size(size)

        return html.option({'value': size, 'onclick': onclick}, f"Show {size}")


    @component
    def PageSizeSelect(sizes:List[int]):

        @event
        def on_change(event):
            paginator.set_page_size(event['currentTarget']['value'])

        @component
        def PageOption(size:int):
            return html.option({'value': size}, f"Show {size}")

        return html.select({'value': sizes[0], "on_change": on_change}, For(PageOption, sizes))


    @component
    def PageInput():

        count_value, set_count = use_state(0)

        @event(prevent_default=True)
        def on_change(event):

            try:
                new_value = int(event['currentTarget']['value'])
                new_value = max(new_value, 1)
                new_value = min(new_value, paginator.page_count)
            except Exception:
                new_value = 1

            log.info('new_value = %d', new_value)

            if (paginator.page_index != new_value - 1):
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
def Text(*children):
    """Add the pico button margin to make the 
    given text line up with the button text."""

    return html.span({'style': 'margin-bottom: var(--spacing);'}, *children)


@component
def THead(columns: List[str]):
    return html.thead(
        For(html.th, iterator=columns)
    )


@component
def TColgroup(col_widths):
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
def TFoot(columns: List[str]):
    return html.tfoot(
        For(html.td, columns)
    )


@component
def AppMain():

    table_data = use_memo(lambda: make_products(9999))

    table = use_reactpy_table(Options(
        data=table_data,
        cols = COLS,
        plugins=[SimplePaginator.init]
    ))


    return html.div(
        html.table({"role": "grid"},
            TColgroup([80, 150, 100, 100, 100, 100]),
            THead(COLS),
            TBody(table.paginator.rows),
            TFoot(COLS),
        ),
        TablePaginator(table.paginator)
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(AppMain)
