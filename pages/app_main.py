from reactpy import component, html
from reactpy_router import route, simple

# import { Component, splitProps } from 'solid-js'
# import { Router, Routes, Route } from '@solidjs/router'

from .components.side_bar import SideBar
from .components.top_bar import TopBar
from .components.footer import Footer
from .components.copyright import Copyright

from .dashboard_page import Dashboard
from .users import Users
from .products import Products

from .sign_in import SignIn
from .sign_up import SignUp
from .components.mobile_logic import SideBarBackdrop
from .settings.dark_mode import dark_mode
from .components.dark_mode_provider import DarkModeProvider


@component
def PageContainer(page, **props):
    return html.div(
    html.div(
        TopBar(),
        html.div({'class_name': 'flex overflow-hidden bg-white pt-16'},
            SideBar(),
            SideBarBackdrop(),
            html.div({'id': 'main-content', 'class_name': 'relative h-full w-full overflow-y-auto bg-gray-50 lg:ml-64'},
                page(**props),
                html.footer(),
                Copyright()
            )
        )
    )
)


def page_route(path, page):
    element = PageContainer(page)
    return route(path, element)


@component
def AppMain():
    return html.div(
        DarkModeProvider(dark_mode(),
            html.div({'class_name': 'bg-gray-50 text-gray-800'},
                simple.router(
                    page_route("/",Dashboard),
                    page_route("/users", Users),
                    page_route("/products",Products),
                    route("/sign-in", SignIn()),
                    route("/sign-up", SignUp())
                )
            )
        )
    )
