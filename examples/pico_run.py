from typing import Union, Callable
from types import FunctionType
from reactpy import component, html
from reactpy.core.component import Component
from modules.server_options import ServerOptions
from fast_server import run


def pico_run(app: Union[Component, Callable], head:Union[Component, Callable]=None):

    if isinstance(app, FunctionType):
        children = app()
    else:
        children = app

    @component
    def AppMain():
        return html.div({'class_name': 'container, display: flex'},
            html.section(
                children
            )
        )

    run(AppMain, options=ServerOptions(head))
