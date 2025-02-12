from typing import Any
from reactpy import component, html, event

from reactpy.core.component import Component
from reactpy.core.events import EventHandler
from reactpy.core.types import VdomChildren
from utils.unique_sequence import UID

from .icon import ICON

# pylint: disable=line-too-long

@event
def null_event(evt: Any) -> None:
    ...

@component
def TTable(head: Component, body: Component):
    return html.div({'class_name': 'flex flex-col'},
        html.div({'class_name': 'overflow-x-auto'},
            html.div({'class_name': 'align-middle inline-block min-w-full'},
                html.div({'class_name': 'shadow overflow-hidden'},
                    html.table({'class_name': 'table-fixed min-w-full divide-y divide-gray-200'},
                        head,
                        body
                    )
                )
            )
        )
    )


@component
def TBody(*rows: Component):
    return html.tbody({'class_name': 'bg-white table-fixed'},
        html._(*rows)
    )


@component
def THead(*children: VdomChildren):
    return html.thead({'class_name': 'bg-gray-100'},
        *children
    )

@component
def TRow(*children: VdomChildren):
    return html.tr({'key': 999, 'class_name': 'hover:bg-gray-100'},
        *children
    )

@component
def Checkbox(label:str ='checkbox', id:str='', checked:bool = False, on_click: EventHandler = null_event):

    state = 'checked' if checked else ''
    id = id if id else UID('checkbox')

    return html.th({'scope': 'col', 'class_name': 'p-4'},
        html.div({'class_name': 'flex items-center'},
            html.input({'id': id, 'checked': state, 'onclick': on_click, 'aria-describedby': 'checkbox-1', 'type': 'checkbox', 'class_name': 'focus:ring-3 h-4 w-4 rounded border-gray-300 bg-gray-50 focus:ring-cyan-200'}),
            html.label({'html_for': id, 'class_name': 'sr-only'}, label)
        )
    )


@component
def RowCheckbox(label:str ='checkbox', id:str='', checked:bool = False, on_click: EventHandler = null_event):

    state = 'checked' if checked else ''
    id = id if id else UID('checkbox')

    return html.td({'class_name': 'w-4 p-4'},
        html.div({'class_name': 'flex items-center'},
            html.input({'id': id, 'checked': state, 'onclick': on_click, 'aria-describedby': 'checkbox-1', 'type': 'checkbox', 'class_name': 'focus:ring-3 h-4 w-4 rounded border-gray-300 bg-gray-50 focus:ring-cyan-200'}),
            html.label({'html_for': id, 'class_name': 'sr-only'}, label)
        )
    )


@component
def Text(value:str, width:str=""):
    return html.td({'class_name': f'whitespace-nowrap {width} p-4 text-base font-medium text-gray-900'}, value)


@component
def EditButtons(label:str = ''):
    return html.td({'class_name': 'space-x-2 whitespace-nowrap p-4'},
        html.button({'type': 'button', 'data-modal-toggle': 'user-modal', 'class_name': 'inline-flex items-center rounded-lg bg-cyan-600 px-3 py-2 text-center text-sm font-medium text-white hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200'},
            ICON.Edit(),
            f"Edit {label}"
        ),
        html.button({'type': 'button', 'data-modal-toggle': 'delete-user-modal', 'class_name': 'inline-flex items-center rounded-lg bg-red-600 px-3 py-2 text-center text-sm font-medium text-white hover:bg-red-800 focus:ring-4 focus:ring-red-300'},
            ICON.Bin(size='h-5 w-5'),
            f"Delete {label}"
        )
    )

@component
def ColumnHeader(width:int, title:str):
    cls = f'p-4 {width} text-left text-xs font-medium uppercase text-gray-500'
    return html.th({'scope': 'col', 'class_name': cls}, title)
