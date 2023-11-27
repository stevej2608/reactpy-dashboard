from typing import List, Dict
from reactpy import component, html
from utils.logger import log, logging
from examples.pico_run import pico_run

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
    return html.table({"role": "grid"},
        THead(COLS),
        TBody(PRODUCTS),
        TFoot(COLS),
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(AppMain)
