from reactpy import html
from utils.component_class import class_component, ComponentClass
from utils.logger import log, logging
from examples.pico_run import pico_run

GREETING = 'Hello, World!'

@class_component
class Hello(ComponentClass):

    def render(self):
        element = html.h2(GREETING)
        return html.div(
            element
        )

# python -m examples.hello_class

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(Hello)
