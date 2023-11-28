from typing import Union, Callable
from types import FunctionType
from reactpy import html
from reactpy.core.component import Component
from reactpy.backend.fastapi import Options

def ServerOptions(options: Union[Component, Callable]) -> Options:
    """Returns FastAPI server options container"""

    if isinstance(options, FunctionType):
        children = options()
    else:
        children = options

    if not isinstance(children, dict):
        children = children.render()

    return Options(
        head=html.head(children)
    )
