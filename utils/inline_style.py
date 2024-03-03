from reactpy import html


def inline_style(css:str, minify:bool = False):
    """Return html.style tag containing given CSS"""
    if minify:
        css = ' '.join(css.split())
    return html.style({'type': "text/css"}, css)
