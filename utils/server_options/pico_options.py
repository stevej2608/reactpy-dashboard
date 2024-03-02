
from reactpy import html
from .default_options import ServerOptions


PICO_CSS = {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
        'crossorigin': 'anonymous'
    }

PICO_OPTIONS = ServerOptions(
    head=[
        html.link(PICO_CSS)
        ]
)