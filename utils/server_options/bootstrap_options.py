
from reactpy import html
from .default_options import ServerOptions

from .default_options import DEFAULT_OPTIONS

HIGHLIGHT_JS = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11.9.0/styles/default.min.css"
}

HINT_JS = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/hint.css@2.6.0/hint.min.css"
}

BOOTSTRAP_DOCS = {
    "rel": "stylesheet",
    "href": "assets/css/docs.min.css"
}

TEMPLATE = {
    "rel": "stylesheet",
    "href": "assets/css/template.css"
}

BOOTSTRAP_CSS = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
    "integrity": "sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN",
    "crossorigin": "anonymous",
}


FONTAWSOME = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/fontawesome.min.css"
}

BOOTSTRAP_ICONS = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css"
}


BOOTSTRAP_TABLE = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap-table@1.22.2/dist/bootstrap-table.min.css"
}


BOOTSTRAP_SCRIPT = {
    "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
    "integrity": "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
    "crossorigin": "anonymous",
}

BOOTSTRAP_OPTIONS = DEFAULT_OPTIONS + ServerOptions(
    head=[
        html.link(BOOTSTRAP_CSS), 
        html.link(HIGHLIGHT_JS),
        html.link(HINT_JS),
        html.link(BOOTSTRAP_DOCS),
        html.link(TEMPLATE),
        html.link(BOOTSTRAP_CSS),
        html.link(FONTAWSOME),
        html.link(BOOTSTRAP_ICONS),
        html.link(BOOTSTRAP_TABLE),
        html.script(BOOTSTRAP_SCRIPT)
        ]
)
