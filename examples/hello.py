from reactpy import component, html
from utils.logger import log, logging
from examples.pico_main import pico_run

GREETING = 'Hello, World!'

@component
def AppMain():
    element = html.h2(GREETING)
    return html.div(
        element
    )

# python -m examples.hello

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(AppMain)
