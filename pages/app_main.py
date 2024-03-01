from typing import Any

from reactpy import component, html, use_state
from reactpy.core.types import VdomDictConstructor
from reactpy.backend.hooks import use_location
from reactpy_router import Route, route, simple

from utils.logger import log
from utils.types import Props

from .components.app_store import AppContext, AppState, UserSettings
from .components.copyright import Copyright
from .components.dark_mode_provider import DarkModeProvider
from .components.footer import Footer
from .components.mobile_logic import SideBarBackdrop
from .components.side_bar import SideBar
from .components.top_bar import TopBar
from .dashboard_page import Dashboard
from .not_found_404 import NotFoundPage
from .products_page import ProductsPage
from .sign_in import SignIn
from .sign_up import SignUp
from .users_page import UsersPage


@component
def PageContainer(page: VdomDictConstructor, **props: Props):
    return html.div(
        TopBar(),
        html.div({'class_name': 'flex overflow-hidden bg-white pt-16'},
            SideBar(),
            SideBarBackdrop(),
            html.div({'id': 'main-content', 'class_name': 'relative h-full w-full overflow-y-auto bg-gray-50 lg:ml-64'},
                page(**props),
                Footer(),
                Copyright()
            )
        )

    )


def page_route(path: str, page: Any) -> Route:
    element = PageContainer(page)
    return route(path, element)


@component
def AppMain():

    settings, set_settings = use_state(UserSettings())

    location = use_location()
    log.info('location %s', location)
    return AppContext(
        DarkModeProvider(settings.dark_mode,
            html.div({'class_name': 'bg-gray-50 text-gray-800'},
                simple.router(
                    page_route("/",Dashboard),
                    page_route("/users", UsersPage),
                    page_route("/products",ProductsPage),
                    route("/sign-in", SignIn()),
                    route("/sign-up", SignUp()),
                    route("*", NotFoundPage())
                )
            )
        ),
        value = AppState(settings, set_settings)
    )
