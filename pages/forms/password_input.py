from typing import Callable
from reactpy import component, html
from ..components.icon import Icon_EyeSlash, Icon_Eye
from .text_input import Input, Label

def DummyCallable(**argc):
    pass

@component
def PasswordInput(label: str, placeholder="", inputClass:str='', isPasswordVisible:Callable = DummyCallable, setIsPasswordVisible=None, **argc):

    def togglePasswordVisibility():
        return setIsPasswordVisible(lambda visible: not visible)

    icon = Icon_EyeSlash() if isPasswordVisible() else Icon_Eye()

    attributes = {'class_name' : f"pr-8 {inputClass}",
                  'type': isPasswordVisible(),
                  'placeholder': placeholder
                  }

    return html.div(
        Label(label),
        html.div({'class_name': 'relative flex'},
            Input(attributes, **argc),
            html.span({'class_name': 'absolute inset-y-0 right-0 flex items-center pl-2'},
                html.button({'type': 'submit', 'class_name': 'focus:shadow-outline p-1 focus:outline-none', 'onclick': togglePasswordVisibility},
                    icon
                )
            )
        )
    )
