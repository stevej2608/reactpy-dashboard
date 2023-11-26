from typing import Callable
from reactpy import component, html, event

from reactpy_forms import createForm, FieldModel, FormModel, use_form_state
from pages.forms import StandardFormContainer, TextInput, PasswordInput, SubmitButton

from utils.logger import log

class LoginFormData(FormModel):
    email: str = None
    password: str = None
    remember: bool = False


@component
def RememberCheckbox(label=None, field: FieldModel=None, props: Callable = None):

    input_props = props({'type': 'checkbox', 'class_name': 'h-4 w-4 rounded border-gray-300 bg-gray-50', 'required': ''})

    input_props['checked'] = field.value

    return html.div({'class_name': 'flex items-start'},
        html.div({'class_name': 'flex h-5 items-center'},
            html.input(input_props)
        ),
        html.div({'class_name': 'ml-3 text-sm'},
            html.label({'html_for': input_props['name'], 'class_name': 'font-medium text-gray-900'},
                html.a({'href': '#', 'class_name': 'text-teal-500 hover:underline'}, label)
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
def SignIn(*args, **kwargs):

    model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))


    @event(prevent_default=True)
    def handleSubmit(event):
        log.info("Submit [%s]", model)

    Form, Field = createForm(model, set_model)

    log.info("SignIn model=[%s]", model)

    return StandardFormContainer("Sign in to platform",
        Form({'class_name': 'mt-8 space-y-6'},
            Field('email', lambda field, props: TextInput("Your email", props({'placeholder': 'name@company.com'}))),
            Field('password', lambda field, props: PasswordInput("Your password", props())),
            Field('remember', lambda field, props: RememberCheckbox('Remember Me', field, props)),
            SubmitButton(label="Login to your account", onclick=handleSubmit),
            NotRegisteredLink()
        )
    )
