from reactpy import component, html, use_context, event

from .icon import Icon_Sun, Icon_Moon
from .app_store import AppContext
from utils.types import EventArgs

@component
def DarkModeButton():
    settings = use_context(AppContext)

    icon =  Icon_Sun() if settings.dark_mode else Icon_Moon()

    @event
    def onclick(event: EventArgs):
        settings.toggle_dark_mode()

    return html.button({
        'id': 'theme-toggle',
        'type': 'button', 
        'class_name': 'rounded-lg p-2.5 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none',
        'onclick': onclick}, # pylint: disable=unnecessary-lambda
        icon,
    )
