from reactpy import component, html
from reactpy.core.types import VdomChildren
from .icon import Icon_Plus
from utils.child_list import ChildList

@component
def AddButton(label:str):
    return html.button({'type': 'button', 'data-modal-toggle': 'add-user-modal', 'class_name': 'inline-flex w-1/2 items-center justify-center rounded-lg bg-cyan-600 px-3 py-2 text-center text-sm font-medium text-white hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200 sm:w-auto'},
        Icon_Plus(),
        label
    )


@component
def TableTools(*children: VdomChildren):
    return ChildList(*children)
