from reactpy import component, html, use_context

from .icon import Icon_Sun, Icon_Moon
from .app_store import AppContext

@component
def DarkModeButton():
    settings = use_context(AppContext)

    icon =  Icon_Sun() if settings.dark_mode else Icon_Moon()

    return html.button({
        'id': 'theme-toggle',
        'type': 'button', 
        'class_name': 'rounded-lg p-2.5 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none',
        'onclick': lambda : settings.toggle_dark_mode()},
        icon,
    )
