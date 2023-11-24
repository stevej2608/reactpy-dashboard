from reactpy import component, html
from reactpy.svg import svg, path

from .icon import Icon_Bars3CenterLeft, Icon_XMark
                      
@component
def ToggleSidebarMobile():
    return html.button({'id': 'toggleSidebarMobile', 'aria-expanded': 'true', 'aria-controls': 'sidebar', 'class_name': 'mr-2 cursor-pointer rounded p-2 text-gray-600 hover:bg-gray-100 hover:text-gray-900 focus:bg-gray-100 focus:ring-2 focus:ring-gray-100 lg:hidden', 'onclick': '{toggleSidebarMobile}'},
        Icon_Bars3CenterLeft(),
        Icon_XMark()
    )



@component
def MobileSearch():
    return html.button({'id': 'toggleSidebarMobileSearch', 'type': 'button', 'class_name': 'rounded-lg p-2 text-gray-500 hover:bg-gray-100 hover:text-gray-900 lg:hidden', 'onclick': '{toggleSidebarMobile}'},
        html.span({'class_name': 'sr-only'}, "Search"),
        svg({'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewbox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
            path({'fill-rule': 'evenodd', 'd': 'M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', 'clip-rule': 'evenodd'})
        )
    )



@component
def SideBarBackdrop():

    def toggleSidebarMobile():
        print('toggleSidebarMobile')

    return html.div({'id': 'sidebarBackdrop', 'class_name': 'fixed inset-0 z-10 hidden bg-gray-900 opacity-50', 'onclick': toggleSidebarMobile})

