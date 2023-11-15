from reactpy import component, html
from pages.forms.standard_form_container import StandardFormContainer
from pages.forms.text_input import TextInput
from pages.forms.password_input import PasswordInput
from pages.forms.submit_button import SubmitButton

from utils.logger import log


@component
def RememberCheckbox():
    return html.div({'class_name': 'flex items-start'},
        html.div({'class_name': 'flex h-5 items-center'},
            html.input({'name': '{props.name}', 'id': '{props.name}', 'type': 'checkbox', 'class_name': 'h-4 w-4 rounded border-gray-300 bg-gray-50', 'required': ''})
        ),
        html.div({'class_name': 'ml-3 text-sm'},
            html.label({'html_for': '{props.name}', 'class_name': 'font-medium text-gray-900'},
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

    def handleSubmit(event):
        log.info("Submit %o", event)

    return StandardFormContainer("Sign in to platform",
        html.form({'class_name': 'mt-8 space-y-6', 'onsubmit': handleSubmit},
            TextInput(label="Your email", placeholder="name@company.com"),
            PasswordInput(label="Your password", placeholder="••••••••", **argc),
            RememberCheckbox(),
            SubmitButton(label="Login to your account"),
            NotRegisteredLink()
        )
    )
