from typing import Union
from pydantic import field_validator, ValidationInfo
from reactpy import component, html, event
from reactpy.core.events import EventHandler

from reactpy_forms import createForm, FieldModel, FormModel, FieldValidationError, use_form_state
from utils.logger import log, logging
from utils.pico_run import pico_run
from utils.types import Props, EventArgs

class LoginFormData(FormModel):
    email: Union[str, None] = None
    password: Union[str, None] = None

    @field_validator("email")
    @classmethod
    def validate_email(cls, value:str, info: ValidationInfo) -> str:
        if "xxx" == value:
            raise FieldValidationError("xxx is an invalid email!")
        return value


# @component
def TextInput(label: str, field: FieldModel, props: Props):

    # log.info('TextInput [%s]', field)

    return html.p(
        html.label(
            label + ' ',
            html.input(props),
            html.div({'id': f'{field.name}-error'}, field.error)
        )
    )

@component
def SubmitButton(label: str, model: FormModel, onclick: EventHandler):
    return html.input({'type': 'submit', 'value': label, 'disabled': model.has_errors(), 'onclick': onclick})


@component
def LoginForm():

    model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))

    Form, Field = createForm(model, set_model)

    @event(prevent_default=True)
    def onclick(event: EventArgs):
        log.info('SUBMIT [%s]', model)

    return Form(
        html.h2("Login"),
        Field('email', lambda field, props: TextInput('Email', field, props({'id': 'email', 'type':'email'}))),
        Field('password', lambda field, props: TextInput('Password', field, props({'id': 'password'}))),
        SubmitButton('Login', model, onclick=onclick)
    )


# python -m examples.form_login

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(LoginForm)
