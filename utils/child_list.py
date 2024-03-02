from typing import Tuple
from reactpy import component, html
from reactpy.core.component import Component

@component
def ChildList(*children: Tuple[Component]):
    """Assign the child index to the key field

    Returns:
        html._(): Return a fragment containing the children
    """

    for index, child in enumerate(children):
        if not (isinstance(child, dict) or isinstance(child, str)):
            child.key = index # type: ignore

    return html._(*children)
