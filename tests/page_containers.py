from types import FunctionType
from typing import Union, Callable
from reactpy import component, html
from reactpy.core.types import VdomChildren
from reactpy.testing import DisplayFixture


from modules.css_links import PICO_CSS


class PicoContainer:
    """Simple wrapper for the reactpy component being tested"""

    def __init__(self, display:DisplayFixture):
        self.display = display

    async def show(self, app:Union[VdomChildren, Callable]):

        if isinstance(app, FunctionType):
            children = app()
        else:
            children = app

        @component
        def AppContainer():
            return html._(
                html.head(
                    html.link(PICO_CSS)
                ),
                children
            )

        await self.display.show(AppContainer)
