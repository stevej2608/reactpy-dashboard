from reactpy import component, html
from reactpy_router import link

from .icon import (
    Icon_RightFromLine,
    Icon_User,
    Icon_Bag,
    Icon_SignUp,
    Icon_Dashboard,
    Icon_Squares2x2Bold,
    Icon_Inbox,
    Icon_Upgrade,
    Icon_Documentation,
    Icon_Components,
    Icon_Help,
)


@component
def Pro():
    return html.span(
        {
            "class_name": "ml-3 inline-flex items-center justify-center rounded-full bg-gray-200 px-2 text-sm font-medium text-gray-800"
        },
        "Pro",
    )


@component
def SideBarItem(text, icon, path, pro=False):
    pro = Pro() if pro else ""

    button = html.button({'class_name': 'group flex items-center rounded-lg p-2 text-base font-normal text-gray-900 hover:bg-gray-100'},
            icon(),
            html.span({'class_name': 'ml-3 flex-1 whitespace-nowrap'}, text)
            # pro
        )

    return html.li(
        link(button, to=path)
        )

@component
def SideBarLink(text, icon, path):
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
                    Icon_Squares2x2Bold()
                ),
                html.input({'type': 'text', 'name': 'email', 'id': 'mobile-search', 'class_name': 'block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 pl-10 text-sm text-gray-900 focus:ring-cyan-600 focus:ring-cyan-600', 'placeholder': 'Search'})
            )
        )
    )

@component
def SideBar():
    return html.aside({'id': 'sidebar', 'class_name': 'fixed left-0 top-0 z-20 flex hidden h-full w-64 flex-shrink-0 flex-col pt-16 transition-width duration-75 lg:flex', 'aria-label': 'Sidebar'},
        html.div({'class_name': 'relative flex min-h-0 flex-1 flex-col border-r border-gray-200 bg-white pt-0'},
            html.div({'class_name': 'flex flex-1 flex-col overflow-y-auto pb-4 pt-5'},
                html.div({'class_name': 'flex-1 space-y-1 divide-gray-200 divide-y bg-white px-3'},
                    html.ul({'class_name': 'space-y-2 pb-2'},
                        MobileSearch(),
                        SideBarItem(text="Dashboard", icon=Icon_Dashboard, path="/"),
                        # SideBarItem(text="Kanban", pro=True, icon=Icon_Squares2x2Bold, path="/kanban"),
                        # SideBarItem(text="Inbox", pro=True, icon=Icon_Inbox, path="/inbox"),
                        # SideBarItem(text="Users", icon=Icon_User, path="/users"),
                        # SideBarItem(text="Products", icon=Icon_Bag, path="/products"),
                        # SideBarItem(text="Sign In", icon=Icon_RightFromLine, path="/sign-in"),
                        # SideBarItem(text="Sign Up", icon=Icon_SignUp, path="/sign-up")
                    ),
                    html.div({'class_name': 'space-y-2 pt-2'},
                        SideBarLink(text="Upgrade to Pro", icon=Icon_Upgrade, path="https://demo.themesberg.com/windster/pricing/"),
                        SideBarLink(text="Documentation", icon=Icon_Documentation, path="https://flowbite.com/docs/getting-started/introduction/"),
                        SideBarLink(text="Components", icon=Icon_Components, path="https://flowbite.com/docs/components/alerts/"),
                        SideBarLink(text="Help", icon=Icon_Help, path="https://github.com/themesberg/windster-tailwind-css-dashboard/issues")
                    )
                )
            )
        )
    )
