from typing import Optional
from reactpy import component, html, event, use_state
from reactpy_forms import create_form, FieldModel, FormModel, use_form_state
from reactpy_utils.types import EventArgs, NO_PROPS, PropsFunc

from utils.logger import log
from reactpy_utils import DocumentTitle


from .forms import StandardFormContainer, TextInput, PasswordInput, PasswordState, PasswordContext, SubmitButton



class RegisterFormData(FormModel):
    email: Optional[str] = None
    password: Optional[str] = None
    confirm_password: Optional[str] = None
    terms: bool = False


@component
def TermsCheckbox(label:Optional[str]=None, field: Optional[FieldModel]=None, props: PropsFunc = NO_PROPS):

    input_props = props({'type': 'checkbox', 'class_name': 'h-4 w-4 rounded border-gray-300 bg-gray-50', 'required': ''})

    input_props['checked'] = field.value if field else False

    return html.div({'class_name': 'flex items-start'},
        html.div({'class_name': 'flex h-5 items-center'},
            html.input(input_props)
        ),
        html.div({'class_name': 'ml-3 text-sm'},
            html.label({'html_for': input_props['name'], 'class_name': 'font-medium text-gray-900'},
                "I accept the ",
                html.a({'href': '#', 'class_name': 'text-teal-500 hover:underline'}, label if label else '')
            )
        )
    )

@component
def HaveAccountLink():
    return html.div({'class_name': 'text-sm font-medium text-gray-500'},
        " Already have an account? ",
        html.a({'href': '/sign-in', 'class_name': 'text-teal-500 hover:underline'}, "Login here")
    )

@component
def SignUp():

    password_state, set_password_state = use_state(PasswordState())

    model, set_model = use_form_state(RegisterFormData())

    @event(prevent_default=True)
    def handleSubmit(event: EventArgs):
        log.info("Submit [%s]", model)

    Form, Field = create_form(model, set_model)

    log.info("SignUp model=[%s]", model)

    @component
    def SignUpForm():
        return StandardFormContainer("Create a Free Account",
            Form({'class_name': 'mt-8 space-y-6'},
                Field('email', lambda props, field: TextInput("Your email", props({'placeholder': 'name@company.com'}))),
                Field('password', lambda props, field: PasswordInput("Create password", props)),
                Field('confirm_password', lambda props, field: PasswordInput("Confirm password", props)),
                Field('terms', lambda props, field: TermsCheckbox("Terms and Conditions", field, props)),
                SubmitButton(label="Create account", onclick=handleSubmit),
                HaveAccountLink()
            )
        )

    return PasswordContext(
        DocumentTitle("Sign Up - reactpy"),
        SignUpForm(),
        value=(password_state, set_password_state)
        )
