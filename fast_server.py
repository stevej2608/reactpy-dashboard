from typing import Callable
import sys
import signal
import multiprocessing
import uvicorn
from fastapi import FastAPI
from reactpy import html
from reactpy.core.component import Component
from reactpy.backend.fastapi import configure, Options

from utils.logger import log
from utils.var_name import var_name

from modules.assets import assets_api
from modules.tailwind import TAILWIND_CSS

app = FastAPI(description="ReactPy", version="0.1.0")


PAGE_HEADER_TITLE  = 'ReactPy Dashboard'

GOOGLE_FONTS = {
        'rel': 'preconnect',
        'href': 'https://fonts.googleapis.com'
    }

GOOGLE_STATIC_FONTS = {
        'rel': 'preconnect',
        'href': 'https://fonts.gstatic.com',
        'crossorigin': ''
    }

GOOGLE_CSS = {
        'rel': 'stylesheet',
        'href': 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap'
    }

META_VIEWPORT = {
    'name': "viewport",
    'content': "width=device-width",
    'initial-scale': 1
    }

META_COLOR = {
    'theme-color': "viewport",
    'content': "#000000"
    }

DASHBOARD_OPTIONS=Options(
    head=html.head(
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        html.link(GOOGLE_FONTS),
        html.link(GOOGLE_STATIC_FONTS),
        html.link(GOOGLE_CSS),
        html.title(PAGE_HEADER_TITLE),
        html.link(TAILWIND_CSS),
    )
)

def handler(signum, frame):
    active = multiprocessing.active_children()
    for child in active:
        child.terminate()
 
def run(AppMain: Callable[[], Component], options:Options=DASHBOARD_OPTIONS, **kwargs) -> None:
    """Called once to run reactpy application on the fastapi server

    Args:
        AppMain (Callable[[], Component]): Function that returns a reactpy Component
        options (Options, optional): Server options. Defaults to DASHBOARD_OPTIONS.

    Usage:
    ```
            @component
            def AppMain():
                return html.h2('Hello from reactPy!')
                )

            run(AppMain, options=PICO_OPTIONS)

    ```
    """

    def _app_path(app: FastAPI) -> str:
        app_str = var_name(app, globals())
        package_prefix =  __package__ + '.' if __package__ else ''
        return f"{package_prefix}{__name__}:{app_str}"

    # Mount any fastapi end points here

    app.mount('/static', assets_api)

    configure(app, AppMain, options=options)

    app_path = _app_path(app)

    try:
        signal.signal(signal.SIGINT, handler)
        uvicorn.run(app_path, **kwargs)
    finally:
        print('\b\b')
        log.info('Uvicorn server has shut down\n')
        sys.exit(0)

