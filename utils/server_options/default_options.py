from reactpy import html
from .server_options import ServerOptions

_PAGE_HEADER_TITLE = "ReactPy Dashboard"

_GOOGLE_FONTS = {"rel": "preconnect", "href": "https://fonts.googleapis.com"}

_GOOGLE_STATIC_FONTS = {
    "rel": "preconnect",
    "href": "https://fonts.gstatic.com",
    "crossorigin": "",
}

_GOOGLE_CSS = {
    "rel": "stylesheet",
    "href": "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
}

_META_VIEWPORT = {
    "name": "viewport",
    "content": "width=device-width",
    "initial-scale": 1,
}

_META_COLOR = {"theme-color": "viewport", "content": "#000000"}

DEFAULT_OPTIONS = ServerOptions(
    head=[
        html.meta(_META_VIEWPORT),
        html.meta(_META_COLOR),
        html.link(_GOOGLE_FONTS),
        html.link(_GOOGLE_STATIC_FONTS),
        html.link(_GOOGLE_CSS),
        html.title(_PAGE_HEADER_TITLE),
    ]
)
