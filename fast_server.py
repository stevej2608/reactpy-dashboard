import uvicorn
from fastapi import FastAPI
from reactpy import html
from reactpy.core.component import Component
from reactpy.backend.fastapi import configure, Options

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

options=Options(
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


def run(AppMain: Component, **kwargs) -> str:
    """Called once to run the server"""

    def package_prefix():
        return __package__ + '.' if __package__ else ''

    # Mount any fastapi end points here

    app.mount('/static', assets_api)

    configure(app, AppMain, options=options)

    app_path = f"{package_prefix()}{__name__}:app"
    uvicorn.run(app_path, **kwargs)
