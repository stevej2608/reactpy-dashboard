from reactpy import component, html

from .logo import Logo
from .icon import Icon_Search, Icon_Diamond
from .gitHub_button import GitHubButton

from .mobile_logic import ToggleSidebarMobile, MobileSearch
from .dark_mode_button import DarkModeButton
from ..settings.dark_mode import dark_mode


@component
def StarsButton(color):
    return GitHubButton({
        'href': 'https://github.com/themesberg/tailwind-dashboard-windster', 
        'data-text': 'Star', 
        'data-size': 
        'large', 
        'data-show-count': 'true', 
        'data-icon': 'octicon-star', 
        'data-color-scheme': color, 
        'aria-label': 'Star tom-james-watson/p2p.chat on GitHub'}, 
        "Star"
    )


@component
def OpenSource():

    # <GitHubButton /> requests the project star rating from the GitHub website.
    # To avoid network access and flicker when switching between light & dark
    # mode we fetch two version of the button and interchange them in the UI

    StarsDark = StarsButton(color="dark")
    StarsLight = StarsButton(color="light")

    @component
    def DarkModeStarButton():
        return StarsDark if dark_mode() else StarsLight


    return html.div(
    html.div({'class_name': 'hidden items-center lg:flex'},
        html.span({'class_name': 'mr-5 text-base font-normal text-gray-500'}, "Open source ❤️"),
        DarkModeStarButton()
    )
)


@component
def ProUpgrade():
    return html.div(
    html.a({'href': 'https://demo.themesberg.com/windster/pricing/', 'class_name': 'ml-5 mr-3 hidden items-center rounded-lg bg-cyan-600 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200 sm:inline-flex'},
        Icon_Diamond(),
        "Upgrade to Pro"
    )
)

@component
def Search():
    return html.div(
    html.form({'action': '#', 'method': 'GET', 'class_name': 'hidden lg:block lg:pl-32'},
        html.label({'html_for': 'topbar-search', 'class_name': 'sr-only'}, "Search"),
        html.div({'class_name': 'relative mt-1 lg:w-64'},
            html.div({'class_name': 'pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3'},
                Icon_Search()
            ),
            html.input({'type': 'text', 'name': 'email', 'id': 'topbar-search', 'class_name': 'block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 pl-10 text-gray-900 focus:border-cyan-600 focus:ring-cyan-600 sm:text-sm', 'placeholder': 'Search'})
        )
    )
)

@component
def TopBar():
   return html.div(
    html.nav({'class_name': 'fixed z-30 w-full border-b border-gray-200 bg-white'},
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
)
