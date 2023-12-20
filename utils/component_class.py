from typing import Type
from reactpy.core.component import Component


class ComponentClass(Component):

    def __init__(self):
        super().__init__(None, None, None, None, None)


def class_component(comp: Type[ComponentClass]):
    """ReactPy ComponentClass decorator

    Args:
        comp (ComponentClass): Class to be wrapped

    Usage:
    ```
        from reactpy import html, run
        from utils.component_class import class_component, ComponentClass

        @class_component
        class HelloWorld(ComponentClass):

            def render(self):
                return html.h2('Hello World!')

        run(HelloWorld)
    ```
    """

    def create_component(*argv, **kwargs):
        return comp(*argv, **kwargs)

    return create_component
