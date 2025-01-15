from reactpy import component, html, use_context
from reactpy_github_buttons import StarButton

from .app_store import AppContext
from .dark_mode_button import DarkModeButton
from .icon import Icon_Gem, Icon_Search, Icon_Menu


# pylint: disable=line-too-long

@component
def StarsButton(color:str):
    # log.info('StarsButton(%s)', color)

    if color == 'dark':
        scheme = "no-preference: light; light: dark; dark: light_high_contrast;"
    else:
        scheme = "no-preference: light; dark: dark; dark: dark_high_contrast;"

    return html.div({'class_name': '-mb-1'},
        StarButton(user='stevej2608', repo='reactpy-dashboard', large=True, show_count=True, color_scheme=scheme)
    )


@component
def OpenSource():
    settings, _ = use_context(AppContext)

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
    app_state, set_app_state = use_context(AppContext)


    sidebar_open = "left-64" if app_state.sidebar_open else "left-0"
    button_hidden = 'hidden' if app_state.sidebar_open else ''


    return html.header({'class_name': f'bg-white border-b border-gray-200 fixed top-0 right-0 z-20 transition-[left] duration-200 ease-in-out {sidebar_open}'},
        html.div({'class_name': 'flex items-center justify-between h-16 px-4'},

            html.div({'class_name': 'flex items-center gap-3'},

                html.button({'class_name': f'text-gray-500 hover:text-gray-600 {button_hidden}',
                            'on_click': lambda _: set_app_state(app_state.update(sidebar_open=not app_state.sidebar_open))},
                    Icon_Menu()
                ),

                html.h1({'class_name': 'text-xl font-semibold text-gray-800'},
                    Search(),
                ),
            ),


            html.div({'class_name': 'flex items-center gap-4'},
                DarkModeButton(),
            )
        )
    )