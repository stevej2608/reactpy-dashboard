from typing import Optional
from reactpy import component, html, event, use_state
from reactpy_utils.types import EventArgs, NO_PROPS, PropsFunc

from reactpy_forms import create_form, FieldModel, FormModel, use_form_state

from utils.logger import log
from reactpy_utils import DocumentTitle

from .forms import StandardFormContainer, TextInput, PasswordInput, PasswordState, PasswordContext, SubmitButton

class LoginFormData(FormModel):
    email: Optional[str] = None
    password: Optional[str] = None
    remember: bool = False


@component
def RememberCheckbox(
    label: Optional[str] = None,
    field: Optional[FieldModel] = None,
    props: PropsFunc = NO_PROPS,
):

    input_props = props(
        {
            "type": "checkbox",
            "class_name": "h-4 w-4 rounded border-gray-300 bg-gray-50",
            "required": "",
        }
    )

    input_props["checked"] = field.value if field else False

    return html.div(
        {"class_name": "flex items-start"},
        html.div({"class_name": "flex h-5 items-center"}, html.input(input_props)),
        html.div(
            {"class_name": "ml-3 text-sm"},
            html.label(
                {
                    "html_for": input_props["name"],
                    "class_name": "font-medium text-gray-900",
                },
                html.a(
                    {"href": "#", "class_name": "text-teal-500 hover:underline"},
                    label if label else "",
                ),
            ),
        ),
        html.a(
            {
                "href": "#",
                "class_name": "ml-auto text-sm text-teal-500 hover:underline",
            },
            "Lost Password?",
        ),
    )


@component
def NotRegisteredLink():
    return html.div({'class_name': 'text-sm font-medium text-gray-500'},
        " Not registered ",
        html.a({'href': '/sign-up', 'class_name': 'text-teal-500 hover:underline'}, "Create account")
    )

@component
def SignIn():

    password_state, set_password_state = use_state(PasswordState())

    model, set_model = use_form_state(
        LoginFormData(email="joe@gmail.com", password="1234")
    )

    @event(prevent_default=True)
    def handleSubmit(event: EventArgs):
        log.info("Submit [%s]", model)

    Form, Field = create_form(model, set_model)

    log.info("SignIn model=[%s]", model)

    @component
    def SignInForm():
        return StandardFormContainer("Sign in to platform",
            Form({'class_name': 'mt-8 space-y-6'},
                Field('email', lambda props, field: TextInput("Your email", props({'placeholder': 'name@company.com'}))),
                Field('password', lambda props, field: PasswordInput("Your password", props)),
                Field('remember', lambda props, field: RememberCheckbox('Remember Me', field, props)),
                SubmitButton(label="Login to your account", onclick=handleSubmit),
                NotRegisteredLink()
            )
        )

    return PasswordContext(
        DocumentTitle("Sign In - reactpy"),
        SignInForm(),
        value=(password_state, set_password_state)
        )
