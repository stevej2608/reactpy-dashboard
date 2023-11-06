from reactpy import component, html
from utils.logger import log

@component
def MainApp():
    log.info('MainApp - Hello, world!')
    return html.h1("Hello, world!")
