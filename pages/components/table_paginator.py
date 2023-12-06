from reactpy import component, html, event
from reactpy.core.component import Component
from reactpy_table  import Paginator
from utils.child_list import ChildList

from .icon import Icon_LeftBracket, Icon_RightBracket, Icon_LeftBracketSmall, Icon_RightBracketSmall


@component
def Button(icon, label, onclick, disabled):

    def getClass():
        cls="inline-flex flex-1 items-center justify-center rounded-lg bg-cyan-600 px-3 py-2 text-center text-sm font-medium text-white "
        cls += "disabled:opacity-50 disabled:cursor-default" if disabled  else "hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200"
        return cls

    return html.button({'onclick': onclick, 'disabled': disabled, 'class_name': getClass()}, icon(), label + ' ')


@component
def ArrowIcon(icon, onclick, disabled):

    @event
    def _onclick(event):
        onclick()

    def getClass():
        cls="inline-flex cursor-pointer justify-center rounded p-1 text-gray-500 "
        cls += "disabled:opacity-50 disabled:cursor-default" if disabled  else "hover:bg-gray-100 hover:text-gray-900"
        return cls

    return html.button({'onclick': _onclick, 'disabled': disabled, 'class_name': getClass()}, icon())


@component
def Faint (*children: Component):
    return html.span({'class_name':'text-sm font-normal text-gray-500'}, ChildList(*children))


@component
def Bold (text:str):
    return html.span({'class_name':'font-semibold text-gray-900'}, text)


@component
def TablePaginator(paginator: Paginator):

    return html.div({'class_name': 'sticky bottom-0 right-0 w-full items-center border-t border-gray-200 bg-white p-4 sm:flex sm:justify-between'},
        html.div({'class_name': 'mb-4 flex items-center sm:mb-0'},
            ArrowIcon(icon=Icon_LeftBracket, onclick = paginator.previous_page, disabled = not paginator.get_can_previous_page()),
            ArrowIcon(icon=Icon_RightBracket, onclick = paginator.next_page, disabled = not paginator.get_can_next_page()),
            Faint(
                "Showing ",
                Bold(paginator.page_index + 1),
                " of ",
                Bold(paginator.page_count),
                "   "
            ),
        ),
        html.div({'class_name': 'flex items-center space-x-3'},
            Button(label='Previous', icon=Icon_LeftBracketSmall, onclick=paginator.previous_page, disabled=paginator.get_can_previous_page()),
            Button(label='Next', icon=Icon_RightBracketSmall, onclick=paginator.next_page, disabled= not paginator.get_can_next_page())
            )
        )
