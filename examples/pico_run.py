from typing import Union, Callable
from types import FunctionType
from reactpy import component, html
from reactpy.core.types import VdomChildren
from modules.pico import PICO_OPTIONS
from fast_server import run


def pico_run(app: Union[VdomChildren, Callable]):

    if isinstance(app, FunctionType):
        children = app()
    else:
        children = app

    @component
    def AppMain():
        return html.div({'class_name': 'container'},
            html.section(
                children
            )
        )

    run(AppMain, options=PICO_OPTIONS)
