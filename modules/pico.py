from reactpy import html
from reactpy.backend.fastapi import Options

# https://picocss.com/docs/

PICO_CSS = {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
        'crossorigin': 'anonymous'
    }


PICO_OPTIONS=Options(
    head=html.head(
        html.link(PICO_CSS)
    )
)
