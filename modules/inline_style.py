from reactpy import html


def inline_style(CSS:str, minify:bool = False):
    """Return html.style tag containing given CSS"""
    if minify:
        CSS = ' '.join(CSS.split())
    return html.style({'type': "text/css"}, CSS)
