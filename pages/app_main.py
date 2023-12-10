from reactpy import component, html
from reactpy.backend.hooks import use_location
from reactpy_router import route, simple

from .components.side_bar import SideBar
from .components.top_bar import TopBar
from .components.footer import Footer
from .components.copyright import Copyright

from .dashboard_page import Dashboard
from .users_page import UsersPage
from .products_page import ProductsPage
from .not_found_404 import NotFoundPage

from .sign_in import SignIn
from .sign_up import SignUp
from .components.mobile_logic import SideBarBackdrop
from .settings.dark_mode import dark_mode
from .components.dark_mode_provider import DarkModeProvider

from utils.logger import log


@component
def PageContainer(page, **props):
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


def page_route(path, page):
    element = PageContainer(page)
    return route(path, element)


@component
def AppMain():
    location = use_location()
    log.info('location %s', location)
    return DarkModeProvider(dark_mode(),
        html.div({'class_name': 'bg-gray-50 text-gray-800'},
            simple.router(
                page_route("/",Dashboard),
                page_route("/users", UsersPage),
                page_route("/products",ProductsPage),
                route("/sign-in", SignIn()),
                route("/sign-up", SignUp()),
                route("/not-found", NotFoundPage()),
                # route("*", NoFoundPage())
            )
        )
    )
