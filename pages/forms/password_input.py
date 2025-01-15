from inspect import isfunction
from typing import cast
from reactpy import component, event, html, use_context

from reactpy_utils.dynamic_context import DynamicContextModel, create_dynamic_context
from reactpy_utils.types import EventArgs, Props, PropsFunc

from ..components.icon import ICON
from .text_input import Input, Label


class PasswordState(DynamicContextModel):
    show: bool = False

PasswordContext = create_dynamic_context(PasswordState)


# https://github.com/RWallan/send-email-reactpy/blob/main/frontend/src/pages/formPage.py


@component
def PasswordInput(label: str, props: Props | PropsFunc | None = None):
    context, set_context = use_context(PasswordContext)

    props = cast(Props, props({}) if isfunction(props) else {})

    @event(prevent_default=True)
    def toggle_password_visibility(event: EventArgs):
        set_context(lambda ctx: ctx.update(show=not ctx.show))

    icon = ICON.EyeSlash if context.show else ICON.Eye

    _props = {
        'type': 'input' if context.show else 'password',
        **props
        }

    if  'class_name' not in _props:
        _props['class_name'] = ''

    _props['class_name'] =  f"pr-8 {_props['class_name']}"

    return html.div(
        Label(label),
        html.div({'class_name': 'relative flex'},
            Input(_props),
            html.span({'class_name': 'absolute inset-y-0 right-0 flex items-center pl-2'},
                html.button({'type': 'submit', 'class_name': 'focus:shadow-outline p-1 focus:outline-none', 'on_click': toggle_password_visibility},
                    icon()
                )
            )
        )
    )

