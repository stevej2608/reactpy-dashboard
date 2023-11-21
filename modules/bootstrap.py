from reactpy import html
from reactpy.backend.fastapi import Options

# https://getbootstrap.com/docs/4.4/getting-started/introduction/

BOOTSTRAP_CSS = {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css',
        'crossorigin': 'anonymous'
    }


BOOTSTRAP_OPTIONS=Options(
    head=html.head(
        html.link(BOOTSTRAP_CSS),
    )
)
