from typing import Any

from reactpy import component, html, use_state
from reactpy.backend.hooks import use_location
from reactpy_router import Route, route, simple

from utils.logger import log
from utils.fast_server import run

from utils.server_options.dashboard_options import DASHBOARD_OPTIONS

from pages import Dashboard, NotFoundPage, ProductsPage, SignIn, SignUp, UsersPage, PageContainer
from pages.components import AppContext, AppState, UserSettings, DarkModeProvider


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


# python app_main.py

if __name__ == "__main__":
    run(AppMain, options=DASHBOARD_OPTIONS)
