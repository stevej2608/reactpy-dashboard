from reactpy import html

def InlineStyle(CSS:str, minify:bool = False):
    if minify:
        CSS = ' '.join(CSS.split())
    return html.style({'type': "text/css"}, CSS)
