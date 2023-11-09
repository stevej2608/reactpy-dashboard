from reactpy import component, html

from .icon import Icon_Sun, Icon_Moon
from ..settings.dark_mode import dark_mode

@component
def DarkModeButton():

    icon = Icon_Sun() if dark_mode() else Icon_Moon()

    return html.div(
    html.button({'id': 'theme-toggle', 'type': 'button', 'class_name': 'rounded-lg p-2.5 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none', 'onclick': '{toggleDarkMode}'},
        icon,
    )
)
