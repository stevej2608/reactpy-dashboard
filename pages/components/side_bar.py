from typing import cast, Any
from reactpy import component, html, use_context
from reactpy.types import VdomDict
from reactpy_router import link

from .app_store import AppContext
from .logo import Logo

from .icon import Icon, ICON


# pylint: disable=line-too-long

@component
def Pro():
    return html.span({"class_name": "ml-3 inline-flex items-center justify-center rounded-full bg-gray-200 px-2 text-sm font-medium text-gray-800"},
        "Pro"
    )


@component
def SideBarItem(text: str, icon: Icon, path: str, is_pro: bool=False):

    def vdom_dict(comp: Any) -> VdomDict:
        icon_comp = comp()
        return cast(VdomDict, icon_comp.type())

    return html.li(
        link({'to': path},
            html.div({'class_name': 'group flex items-center rounded-lg p-2 text-base font-normal text-gray-900 hover:bg-gray-100'},
                vdom_dict(icon),
                html.span({'class_name': 'ml-3 flex-1 whitespace-nowrap'}, text),
                vdom_dict(Pro) if is_pro else ""
                )
            )
    )


@component
def SideBarLink(text: str, icon: Icon, path: str):
    return html.a({'href': path, 'class_name': 'group flex items-center rounded-lg p-2 text-base font-normal text-gray-900 transition duration-75 hover:bg-gray-100', 'target': '_blank'},
        icon(),
        html.span({'class_name': 'ml-3'}, text)
    )

@component
def MobileSearch():
    return html.li(
        html.form({'action': '#', 'method': 'GET', 'class_name': 'lg:hidden'},
            html.label({'html_for': 'mobile-search', 'class_name': 'sr-only'}, "Search"),
            html.div({'class_name': 'relative'},
                html.div({'class_name': 'pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3'},
                    ICON.Squares2x2Bold()
                ),
                html.input({'type': 'text', 'name': 'email', 'id': 'mobile-search', 'class_name': 'block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 pl-10 text-sm text-gray-900 focus:ring-cyan-600 focus:ring-cyan-600', 'placeholder': 'Search'})
            )
        )
    )

@component
def SideBar():
    app_state, set_app_state = use_context(AppContext)

    # closed = fixed top-0 left-0 h-full w-64 bg-white border-r border-gray-200 transform transition-transform duration-200 ease-in-out z-30 -translate-x-full
    # open   = fixed top-0 left-0 h-full w-64 bg-white border-r border-gray-200 transform transition-transform duration-200 ease-in-out z-30

    sidebar_open = '' if app_state.sidebar_open else '-translate-x-full'
    button_hidden = 'hidden' if app_state.sidebar_open is False else ''

    return html.aside({"id": "sidebar",
            "class_name": f"fixed top-0 left-0 h-full w-64 bg-white border-r border-gray-200 transform transition-transform duration-200 ease-in-out z-30 {sidebar_open}",
            "aria-label": "Sidebar",
        },


        html.div({'class_name': 'flex items-center justify-between h-16 px-4 border-b border-gray-200'},
            Logo(),
            html.button({'class_name': f'text-gray-500 hover:text-gray-700 {button_hidden}',
                'on_click': lambda _: set_app_state(app_state.update(sidebar_open=not app_state.sidebar_open))},
                ICON.XMark()
            )
        ),



        html.div({'class_name': 'relative flex min-h-0 flex-1 flex-col border-r border-gray-200 bg-white pt-0'},
            html.div({'class_name': 'flex flex-1 flex-col overflow-y-auto pb-4 pt-5'},
                html.div({'class_name': 'flex-1 space-y-1 divide-gray-200 divide-y bg-white px-3'},
                    html.ul({'class_name': 'space-y-2 pb-2'},
                        MobileSearch(),
                        SideBarItem(text="Dashboard", icon=ICON.Dashboard, path="/"),
                        SideBarItem(text="Kanban", icon=ICON.Squares2x2Bold, path="/kanban", is_pro=True),
                        SideBarItem(text="Inbox", icon=ICON.Inbox, path="/inbox", is_pro=True),
                        SideBarItem(text="Users", icon=ICON.User, path="/users"),
                        SideBarItem(text="Products", icon=ICON.Bag, path="/products"),
                        SideBarItem(text="Sign In", icon=ICON.RightFromLine, path="/sign-in"),
                        SideBarItem(text="Sign Up", icon=ICON.SignUp, path="/sign-up")
                    ),
                    html.div({'class_name': 'space-y-2 pt-2'},
                        SideBarLink(text="Upgrade to Pro", icon=ICON.Upgrade, path="https://demo.themesberg.com/windster/pricing/"),
                        SideBarLink(text="Documentation", icon=ICON.Documentation, path="https://flowbite.com/docs/getting-started/introduction/"),
                        SideBarLink(text="Components", icon=ICON.Components, path="https://flowbite.com/docs/components/alerts/"),
                        SideBarLink(text="Help", icon=ICON.Help, path="https://github.com/themesberg/windster-tailwind-css-dashboard/issues")
                    )
                )
            )
        )
    )
