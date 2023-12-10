from typing import Callable
from reactpy import component, html

@component
def ButtonWithIcon(text: str, icon: Callable):
    _icon = icon().type()
    return html.div({'class_name': 'w-1/2 text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-4 focus:ring-cyan-200 font-medium inline-flex items-center justify-center rounded-lg text-sm px-3 py-2 text-center sm:w-auto'},
        _icon,
        text)
