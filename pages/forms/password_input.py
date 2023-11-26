from reactpy import component, html, use_state, event
from utils.logger import log
from ..components.icon import Icon_EyeSlash, Icon_Eye
from .text_input import Input, Label

# https://github.com/RWallan/send-email-reactpy/blob/main/frontend/src/pages/formPage.py

def DummyCallable(**argc):
    pass

@component
def PasswordInput(label: str, props: dict, password_visible=False):

    _password_visible, set_password_visible = use_state(password_visible)

    @event(prevent_default=True)
    def toggle_password_visibility(event):
        set_password_visible( not _password_visible)

    icon = Icon_EyeSlash if _password_visible else Icon_Eye

    _props = {'type': 'input' if _password_visible else 'password', **props}

    if not 'class_name' in _props:
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
