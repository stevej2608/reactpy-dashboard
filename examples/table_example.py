from typing import List, Dict
from reactpy import component, html
from utils.logger import log, logging
from examples.pico_run import pico_run
from modules.inline_style import inline_style
from modules.css_links import PICO_CSS

# https://codesandbox.io/p/devbox/tanstack-table-example-expanding-jr4nn3?embed=1

CSS= """
html {
  font-family: sans-serif;
  font-size: 14px;
}

table {
  border: 1px solid lightgray;
}

tbody {
  border-bottom: 1px solid lightgray;
}

th {
  border-bottom: 1px solid lightgray;
  border-right: 1px solid lightgray;
  padding: 2px 4px;
}

tfoot {
  color: gray;
}

tfoot th {
  font-weight: normal;
}

"""

@component
def AppHead():
    return html._(
        html.link(PICO_CSS),
        inline_style(CSS)
    )


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

COLS = ['#', 'name', 'description', 'technology', 'ID', 'price']

# https://medium.com/@jordammendes/build-powerfull-tables-in-reactjs-with-tanstack-9d57a3a63e35
# https://tanstack.com/table/v8/docs/examples/react/expanding

@component
def TablePaginator():
    return html.div({'class_name': 'flex items-center gap-2'},

        html.button({'class_name': 'border rounded p-1', 'disabled': ''}, "<<"),
        html.button({'class_name': 'border rounded p-1', 'disabled': ''}, "<"),
        html.button({'class_name': 'border rounded p-1'}, ">"),
        html.button({'class_name': 'border rounded p-1'}, ">>"),

        html.span({'class_name': 'flex items-center gap-1'},
            html.div("Page"),
            html.strong("1 of 10")
        ),

        html.span({'class_name': 'flex items-center gap-1'},
            "| Go to page:",
            html.input({'type': 'number', 'class_name': 'border p-1 rounded w-16', 'value': '1'})
        ),

        html.select(
            html.option({'value': '10'}, "Show 10"),
            html.option({'value': '20'}, "Show 20"),
            html.option({'value': '30'}, "Show 30"),
            html.option({'value': '40'}, "Show 40"),
            html.option({'value': '50'}, "Show 50")
        )
    )


@component
def THead(columns: List[str]):
    return html.thead(
        *list(map(lambda name: html.th({'scope': 'col'}, name), columns))
    )


def TRow(index: int, row: Dict):
    return  html.tr(
        html.th({'scope': 'row'}, index),
        *list(map(html.td, row.values()))
    )


def TBody(data: List[dict]):
    return  html.tbody(
        *[TRow(index, value) for index, value in enumerate(data)]
    )


@component
def TFoot(columns: List[str]):
    return html.tfoot(
        *list(map(lambda name: html.td({'scope': 'col'}, name), columns))
    )

@component
def AppMain():
    return html.div(
        html.table({"role": "grid"},
            THead(COLS),
            TBody(PRODUCTS),
            TFoot(COLS),
        ),
        TablePaginator()
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    # pico_run(AppMain, head=[html.link(PICO_CSS), InlineStyle(CSS)])
    # pico_run(AppMain, head=[html.link(PICO_CSS)])
    pico_run(AppMain, head=AppHead)
