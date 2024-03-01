from reactpy import component, html, use_context
from reactpy_github_buttons import StarButton

from utils.logger import log

from .app_store import AppContext
from .dark_mode_button import DarkModeButton
from .icon import Icon_Gem, Icon_Search
from .logo import Logo
from .mobile_logic import MobileSearch, ToggleSidebarMobile

# pylint: disable=line-too-long

@component
def StarsButton(color:str):
    log.info('StarsButton(%s)', color)

    if color == 'dark':
        scheme = "no-preference: light; light: dark; dark: light_high_contrast;"
    else:
        scheme = "no-preference: light; dark: dark; dark: dark_high_contrast;"

    return html.div({'class_name': '-mb-1'},
        StarButton(user='themesberg', repo='tailwind-dashboard-windster', large=True, show_count=True, color_scheme=scheme)
    )


@component
def OpenSource():
    settings = use_context(AppContext)

    # <GitHubButton /> requests the project star rating from the GitHub website.
    # To avoid network access and flicker when switching between light & dark
    # mode we fetch two version of the button and interchange them in the UI

    StarsDark = StarsButton(color="dark")
    StarsLight = StarsButton(color="light")

    @component
    def DarkModeStarButton():
        return StarsDark if settings.dark_mode else StarsLight


    return html.div({'class_name': 'hidden items-center lg:flex'},
        html.span({'class_name': 'mr-5 text-base font-normal text-gray-500'}, "Open source ❤️"),
        DarkModeStarButton()
    )


@component
def ProUpgrade():
    return html.a({'href': 'https://demo.themesberg.com/windster/pricing/', 'class_name': 'ml-5 mr-3 hidden items-center rounded-lg bg-cyan-600 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200 sm:inline-flex'},
        Icon_Gem(),
        "Upgrade to Pro"
    )

@component
def Search():
    return html.form({'action': '#', 'method': 'GET', 'class_name': 'hidden lg:block lg:pl-32'},
        html.label({'html_for': 'topbar-search', 'class_name': 'sr-only'}, "Search"),
        html.div({'class_name': 'relative mt-1 lg:w-64'},
            html.div({'class_name': 'pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3'},
                Icon_Search()
            ),
            html.input({'type': 'text', 'name': 'email', 'id': 'topbar-search', 'class_name': 'block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 pl-10 text-gray-900 focus:border-cyan-600 focus:ring-cyan-600 sm:text-sm', 'placeholder': 'Search'})
        )
    )


@component
def TopBar():
    return html.nav({'class_name': 'fixed z-30 w-full border-b border-gray-200 bg-white'},
        html.div({'class_name': 'px-3 py-3 lg:px-5 lg:pl-3'},
            html.div({'class_name': 'flex items-center justify-between'},
                html.div({'class_name': 'flex items-center justify-start'},
                    ToggleSidebarMobile(),
                    Logo(),
                    Search()
                ),
                html.div({'class_name': 'flex items-center'},
                    MobileSearch(),
                    OpenSource(),
                    ProUpgrade(),
                    DarkModeButton()
                )
            )
        )
    )
