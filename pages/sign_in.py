from reactpy import component, html, event
from pages.forms.standard_form_container import StandardFormContainer
from pages.forms.text_input import TextInput
from pages.forms.password_input import PasswordInput
from pages.forms.submit_button import SubmitButton

from utils.logger import log


@component
def RememberCheckbox(name=''):
    return html.div({'class_name': 'flex items-start'},
        html.div({'class_name': 'flex h-5 items-center'},
            html.input({'name': name, 'id': name, 'type': 'checkbox', 'class_name': 'h-4 w-4 rounded border-gray-300 bg-gray-50', 'required': ''})
        ),
        html.div({'class_name': 'ml-3 text-sm'},
            html.label({'html_for': name, 'class_name': 'font-medium text-gray-900'},
                html.a({'href': '#', 'class_name': 'text-teal-500 hover:underline'}, "Remember me")
            )
        ),
        html.a({'href': '#', 'class_name': 'ml-auto text-sm text-teal-500 hover:underline'}, "Lost Password?")
    )

@component
def NotRegisteredLink():
    return html.div({'class_name': 'text-sm font-medium text-gray-500'},
        " Not registered ",
        html.a({'href': '/sign-up/', 'class_name': 'text-teal-500 hover:underline'}, "Create account")
    )


@component
def SignIn(**argc):
    log.info("SignIn")

    @event(prevent_default=True)
    def handleSubmit(event):
        log.info("SignIn - Submit")

    log.info("SignIn - render")

    return StandardFormContainer("Sign in to platform",
        html.div({'class_name': 'mt-8 space-y-6'},
            TextInput(label="Your email", placeholder="name@company.com"),
            PasswordInput(label="Your password", placeholder="••••••••", **argc),
            RememberCheckbox(name='remember'),
            SubmitButton(label="Login to your account", onclick=handleSubmit),
            NotRegisteredLink()
        )
    )
