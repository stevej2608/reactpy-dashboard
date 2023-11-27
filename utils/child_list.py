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
        if not isinstance(child, dict):
            child.key = index

    return html._(*children)
