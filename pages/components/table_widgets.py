from reactpy import component, html, event
from reactpy.core.events import EventHandler
from reactpy.core.component import Component
from reactpy.core.types import VdomChildren
from utils.child_list import ChildList

from .icon import Icon_Edit, Icon_Bin


@event
def null_event(evt):
    ...

@component
def Table(head: Component, body: Component):
    return html.table({'class_name': 'min-w-full table-fixed divide-y divide-gray-200'},
        head,
        body
    )


@component
def TBody(*rows: Component):
    return html.tbody({'class_name': 'bg-white table-fixed'},
        html._(*rows)
    )


@component
def THead(*children: VdomChildren):
    return html.thead({'class_name': 'bg-gray-100'},
        ChildList(*children)
    )

@component
def TRow(*children: VdomChildren):
    return html.tr({'key': 999, 'class_name': 'hover:bg-gray-100'},
        ChildList(*children)
    )

@component
def Checkbox(label ='checkbox', checked = False, on_click = null_event):

    state = 'checked' if checked else ''

    return html.th({'scope': 'col', 'class_name': 'p-4 w-[50px]'},
        html.div({'class_name': 'flex items-center'},
            html.input({'id': label, 'checked': state, 'onclick': on_click, 'aria-describedby': 'checkbox-1', 'type': 'checkbox', 'class_name': 'focus:ring-3 h-4 w-4 rounded border-gray-300 bg-gray-50 focus:ring-cyan-200'}),
            html.label({'html_for': label, 'class_name': 'sr-only'}, "checkbox")
        )
    )

@component
def RowCheckbox():
    return html.td({'class_name': 'w-4 p-4'},
        html.div({'class_name': 'flex items-center'},
            html.input({'id': 'checkbox-1', 'aria-describedby': 'checkbox-1', 'type': 'checkbox', 'class_name': 'focus:ring-3 h-4 w-4 rounded border-gray-300 bg-gray-50 focus:ring-cyan-200'}),
            html.label({'html_for': 'checkbox-1', 'class_name': 'sr-only'}, "checkbox")
        )
    )


@component
def Text(value:str):
    return html.td({'class_name': 'whitespace-nowrap p-4 text-base font-medium text-gray-900'}, value)


@component
def EditButtons():
    return html.td({'class_name': 'space-x-2 whitespace-nowrap p-4'},
        html.button({'type': 'button', 'data-modal-toggle': 'user-modal', 'class_name': 'inline-flex items-center rounded-lg bg-cyan-600 px-3 py-2 text-center text-sm font-medium text-white hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200'},
            Icon_Edit(),
            "Edit user"
        ),
        html.button({'type': 'button', 'data-modal-toggle': 'delete-user-modal', 'class_name': 'inline-flex items-center rounded-lg bg-red-600 px-3 py-2 text-center text-sm font-medium text-white hover:bg-red-800 focus:ring-4 focus:ring-red-300'},
            Icon_Bin(),
            "Delete user"
        )
    )

@component
def ColumnHeader(width:int, title:str):
    cls = f'p-4 w-[{width}] text-left text-xs font-medium uppercase text-gray-500'
    return html.th({'scope': 'col', 'class_name': cls}, title)
