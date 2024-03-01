from reactpy import component, event, html, use_state

from utils.types import EventArgs, Props

from ..components.icon import Icon_Eye, Icon_EyeSlash
from .text_input import Input, Label

# https://github.com/RWallan/send-email-reactpy/blob/main/frontend/src/pages/formPage.py

@component
def PasswordInput(label: str, props: Props, password_visible:bool=False):

    _password_visible, set_password_visible = use_state(password_visible)

    @event(prevent_default=True)
    def toggle_password_visibility(event: EventArgs):
        set_password_visible( not _password_visible)

    icon = Icon_EyeSlash if _password_visible else Icon_Eye

    _props = {'type': 'input' if _password_visible else 'password', **props}

    if  'class_name' not in _props:
        _props['class_name'] = ''

    _props['class_name'] =  f"pr-8 {_props['class_name']}"

    return html.div(
        Label(label),
        html.div({'class_name': 'relative flex'},
            Input(_props),
            html.span({'class_name': 'absolute inset-y-0 right-0 flex items-center pl-2'},
                html.button({'type': 'submit', 'class_name': 'focus:shadow-outline p-1 focus:outline-none', 'onclick': toggle_password_visibility},
                    icon()
                )
            )
        )
    )
