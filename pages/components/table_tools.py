from reactpy import component, html
from reactpy.core.types import VdomChildren
from .icon import Icon_Plus
from utils.child_list import ChildList

@component
def AddButton(label:str):
    return html.button({
            'type': 'button', 
            'data-modal-toggle': 'add-user-modal', 
            'class_name': 'text-white bg-cyan-600 hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200 font-medium inline-flex items-center rounded-lg text-sm px-3 py-2 text-center sm:ml-auto'},
        Icon_Plus(),
        label
    )


@component
def TableTools(*children: VdomChildren):
    return html.div({'class_name': 'block sm:flex items-center md:divide-x md:divide-gray-100'},
        ChildList(*children)
    )
