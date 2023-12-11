from reactpy import component, html, use_context

from .icon import Icon_Sun, Icon_Moon
from .app_store import AppContext

@component
def DarkModeButton():
    settings = use_context(AppContext)

    icon =  Icon_Moon() if settings.dark_mode else Icon_Sun()

    return html.button({
        'id': 'theme-toggle',
        'type': 'button', 
        'class_name': 'rounded-lg p-2.5 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none',
        'onclick': lambda event: settings.toggle_dark_mode()},
        icon,
    )
