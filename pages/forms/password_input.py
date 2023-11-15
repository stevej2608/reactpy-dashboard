from reactpy import component, html, use_state, event
from utils.logger import log
from ..components.icon import Icon_EyeSlash, Icon_Eye
from .text_input import Input, Label

# https://github.com/RWallan/send-email-reactpy/blob/main/frontend/src/pages/formPage.py

def DummyCallable(**argc):
    pass

@component
def PasswordInput(label: str, placeholder="", inputClass:str='', isPasswordVisible=False, set_password_visible=None, **argc):

    log.info("PasswordInput")

    password_visible, set_password_visible = use_state(isPasswordVisible)

    @event(prevent_default=True)
    def toggle_password_visibility(event):
        log.info("toggle_password_visibility %s", password_visible)
        set_password_visible( not password_visible)

    icon = Icon_EyeSlash if password_visible else Icon_Eye

    attributes = {'class_name' : f"pr-8 {inputClass}",
                  'type': 'input' if password_visible else 'password',
                  'placeholder': placeholder
                  }

    log.info("PasswordInput - render")

    return html.div(
        Label(label),
        html.div({'class_name': 'relative flex'},
            Input(attributes, **argc),
            html.span({'class_name': 'absolute inset-y-0 right-0 flex items-center pl-2'},
                html.button({'type': 'submit', 'class_name': 'focus:shadow-outline p-1 focus:outline-none', 'onclick': toggle_password_visibility},
                    icon()
                )
            )
        )
    )
