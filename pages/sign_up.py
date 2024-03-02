from typing import Optional, Any
from reactpy import component, html, event

from reactpy_forms import createForm, FieldModel, FormModel, use_form_state
from pages.forms import StandardFormContainer, TextInput, PasswordInput, SubmitButton

from utils.logger import log
from utils.types import EventArgs, NO_PROPS, PropsFunc

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
        html.a({'href': '/sign-in/', 'class_name': 'text-teal-500 hover:underline'}, "Login here")
    )

@component
def SignUp(*args:Any, **kwargs:Any):

    model, set_model = use_form_state(RegisterFormData())

    @event(prevent_default=True)
    def handleSubmit(event: EventArgs):
        log.info("Submit [%s]", model)

    Form, Field = createForm(model, set_model)

    log.info("SignUp model=[%s]", model)


    return StandardFormContainer("Create a Free Account",
        Form({'class_name': 'mt-8 space-y-6'},
            Field('email', lambda field, props: TextInput("Your email", props({'placeholder': 'name@company.com'}))),
            Field('password', lambda field, props: PasswordInput("Your password", props())),
            Field('confirm_password', lambda field, props: PasswordInput("Your password", props())),
            Field('terms', lambda field, props: TermsCheckbox("Terms and Conditions", field, props)),
            SubmitButton(label="Create account", onclick=handleSubmit),
            HaveAccountLink()
        )
    )
