import uvicorn
from fastapi import FastAPI
from reactpy import html, run
from reactpy.backend.fastapi import configure, Options

from pages.app_main import AppMain

from modules.assets import assets_api
from modules.tailwind import TAILWIND_CSS

app = FastAPI(description="ReactPy", version="0.1.0")


PAGE_HEADER_TITLE  = 'ReactPy Dashboard'

options=Options(
    head=html.head(
        html.link(TAILWIND_CSS),
        html.title(PAGE_HEADER_TITLE)
    )
)

def init_fastapp(**kwargs) -> str:
    """Called once, just before server is started"""

    def package_prefix():
        return __package__ + '.' if __package__ else ''

    # Mount any fastapi end points here

    app.mount('/static', assets_api)

    configure(app, AppMain, options=options)

    app_path = f"{package_prefix()}{__name__}:app"
    uvicorn.run(app_path, **kwargs)
