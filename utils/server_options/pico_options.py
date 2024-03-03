
from reactpy import html
from .default_options import ServerOptions

from .default_options import DEFAULT_OPTIONS

PICO_CSS = {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
        'crossorigin': 'anonymous'
    }

PICO_OPTIONS = DEFAULT_OPTIONS + ServerOptions(
    head=[
        html.link(PICO_CSS)
        ]
)