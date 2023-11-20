from pydantic import BaseModel, validator
from reactpy import component, html, run

from utils.logger import log, logging
from reactpy_forms import createForm, FieldModel, FieldValidationError, use_form_state

class LoginFormData(BaseModel):
    email: str = None
    password: str = None


    @validator("email")
    @classmethod
    def validate_email(cls, value):
        if "xxx" == value:
            raise FieldValidationError("xxx is an invalid email!")
        return value


@component
def TextInput(label: str, field: FieldModel, props: dict):
    # log.info('TextInput.%s, error=%s', label, field.error)
    log.info('TextInput [%s]', field)

    return html.p(
        html.label(
            label + ' ',
            html.input(props),
            html.div({'id': 'error'}, field.error)
        )
    )


@component
def AppMain():
    log.info('AppMain')

    model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))

    Form, Field = createForm(model, set_model)
    return Form(
        html.fieldset(
            html.legend("Login"),
            Field('email', lambda field, props: TextInput('Email', field, props({'id': 'email', 'type':'email'}))),
            Field('password', lambda field, props: TextInput('Password', field, props({'id': 'password'})))

        )
    )


# python -m examples.form_login

# Internally app is run by Uvicorn/starlette

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain, host="0.0.0.0", port=8000)
