from typing import cast, Any
from reactpy import component, html
from reactpy.types import VdomDict
from .icon import ICON

# pylint: disable=line-too-long

@component
def ButtonWithIcon(text: str, icon: ICON):

    def vdom_dict(comp: Any) -> VdomDict:
        icon_comp = comp()
        return cast(VdomDict, icon_comp.type())

    return html.div({'class_name': 'w-1/2 text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-4 focus:ring-cyan-200 font-medium inline-flex items-center justify-center rounded-lg text-sm px-3 py-2 text-center sm:w-auto'},
        vdom_dict(icon),
        text)
