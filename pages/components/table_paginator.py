from reactpy import component, html
from reactpy.core.types import VdomChildren
from .reactpy_table  import ReactPyTable

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

    def getClass():
        cls="inline-flex cursor-pointer justify-center rounded p-1 text-gray-500 "
        cls += "disabled:opacity-50 disabled:cursor-default" if disabled  else "hover:bg-gray-100 hover:text-gray-900"
        return cls

    return html.button({'onclick': onclick, 'disabled': disabled, 'class_name': getClass()}, icon())


@component
def Faint (*children: VdomChildren):
    return html.span({'class_name':'text-sm font-normal text-gray-500'}, html._(children))


@component
def Bold (text:str):
    return html.span({'class_name':'font-semibold text-gray-900'}, text)


@component
def TablePaginator(table: ReactPyTable):
    return html.div({'class_name': 'sticky bottom-0 right-0 w-full items-center border-t border-gray-200 bg-white p-4 sm:flex sm:justify-between'},
        html.div({'class_name': 'mb-4 flex items-center sm:mb-0'},
            ArrowIcon(icon=Icon_LeftBracket, onclick = table.previous_page, disabled = not table.get_can_previous_page()),
            ArrowIcon(icon=Icon_RightBracket, onclick = table.next_page, disabled = table.get_can_next_page()),
            Faint(
                "Showing ",
                Bold(table.get_state().pagination.page_index + 1),
                " of ",
                Bold(table.get_page_count()),
                "   "
            ),
        ),
        html.div({'class_name': 'flex items-center space-x-3'},
            Button(label='Previous', icon=Icon_LeftBracketSmall, onclick=table.previous_page, disabled=table.get_can_previous_page()),
            Button(label='Next', icon=Icon_RightBracketSmall, onclick=table.next_page, disabled= not table.get_can_next_page())
            )
        )
