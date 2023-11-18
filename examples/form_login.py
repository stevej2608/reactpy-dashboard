from pydantic import BaseModel, validator
from reactpy import component, html, run

from utils.logger import log, logging
from reactpy_forms import createForm, FieldData

class LoginFormData(BaseModel):
    email: str = None
    password: str = None


    @validator("email")
    @classmethod
    def validate_email(cls, value):
        log.info('validate email=%s', value)
        if "xxx" == value:
            raise ValueError("xxx is an invalid email!")
        return value


@component
def TextInput(label: str, field: FieldData, props: dict):
    log.info('TextInput.%s', label)

    if field.error:
        error_msg = html.div(field.exception.message)
    else:
        error_msg='No Error'

    return html.p(
        html.label(
            label + ' ',
            html.input(props),
            error_msg
        )
    )


@component
def AppMain():

    log.info('AppMain')

    form_data = LoginFormData(email="jones@gmail.com", password="passme99")


    Form, Field, field_data = createForm(form_data)
    return Form(
        html.fieldset(
            html.legend("Login"),
            Field('email', lambda field, props: TextInput('Email', field, props({'type':'email'}))),
            # Field('password', lambda field, props: TextInput('Password', field, props({'type':'password'})))

        )
    )


# python -m examples.form_login

# Internally app is run by Uvicorn/starlette

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain, host="0.0.0.0", port=8000)
