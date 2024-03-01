from types import FunctionType
from typing import Callable, Union, cast

from reactpy import component, html
from reactpy.core.component import Component

from .caller import calling_module_folder
from .fast_server import run
from .server_options import ServerOptions, PICO_OPTIONS


def pico_run(app: Union[Component, Callable[..., Component]], options: ServerOptions | None = None):
    """Wrap the given app in a simple container and call the FastAPI server

    Args:
        app (Union[Component, Callable]): User application
        assets (List[str] | None): CSS and JS assets.

    Returns:
        _type_: _description_
    """
    if isinstance(app, FunctionType):
        children = app()
    else:
        children = cast(Component, app)

    if options is not None:
        options.asset_folder = calling_module_folder()
        options = PICO_OPTIONS + options
    else:
        options = PICO_OPTIONS

    @component
    def AppMain():
        return html.div({"class_name": "container"}, html.section(children))

    run(AppMain, options=options)
