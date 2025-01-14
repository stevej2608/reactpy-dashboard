from typing import Any

from reactpy import component, html, use_state
from reactpy.backend.hooks import use_location
from reactpy_router import  route, browser_router
from reactpy_router.types import Route

from utils.logger import log
from utils.fast_server import run

from utils.server_options import TAILWIND_OPTIONS

from pages import Dashboard, NotFoundPage, ProductsPage, SignIn, SignUp, UsersPage, PageContainer
from pages.components import AppContext, AppState, DarkModeProvider


def page_route(path: str, page: Any) -> Route:
    element = PageContainer(page)
    return route(path, element)


@component
def AppMain():

    settings, set_settings = use_state(AppState())

    location = use_location()
    log.info('location %s', location)
    return AppContext(
        DarkModeProvider(
            html.div({'class_name': 'bg-gray-50 text-gray-800'},
                browser_router(
                    page_route("/",Dashboard),
                    page_route("/users", UsersPage),
                    page_route("/products",ProductsPage),
                    route("/sign-in", SignIn()),
                    route("/sign-up", SignUp()),
                    route("{404:any}", NotFoundPage())
                )
            )
        ),
        value = (settings, set_settings)
    )


# python app_main.py

if __name__ == "__main__":
    run(AppMain, options=TAILWIND_OPTIONS)
