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
def BreadcrumbsAndTitle(*children: VdomChildren):
    return html.div({'class_name': 'mb-4'},
        ChildList(*children)
    )

@component
def TableTools(*children: VdomChildren):
    return html.div({'class_name': 'block sm:flex items-center md:divide-x md:divide-gray-100'},
        ChildList(*children)
    )

@component
def ToolsGroup(*children: VdomChildren):
    return html.div({'class_name': 'flex items-center sm:justify-end w-full'},
        ChildList(*children)
    )

@component
def ButtonContainer(*children: VdomChildren):
    return html.div({'class_name': 'hidden md:flex pl-2 space-x-1'},
        ChildList(*children)
    )


@component
def TableTool(icon):
    return html.a({'href': '#', 'class_name': 'text-gray-500 hover:text-gray-900 cursor-pointer p-1 hover:bg-gray-100 rounded inline-flex justify-center'},
        icon()
    )

@component
def TableSearch():
    return html.form({'class_name': 'sm:pr-3 mb-4 sm:mb-0', 'action': '#', 'method': 'GET'},
        html.label({'html_for': 'products-search', 'class_name': 'sr-only'}, "Search"),
        html.div({'class_name': 'mt-1 relative sm:w-64 xl:w-96'},
            html.input({'type': 'text', 'name': 'email', 'id': 'products-search', 'class_name': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5', 'placeholder': 'Search for products'})
        )
    )
