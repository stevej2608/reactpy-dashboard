from pydantic import BaseModel, validator
from reactpy import component, html, use_state, run

from utils.logger import log, logging
from reactpy_forms import createForm, FieldModel, FieldError

class LoginFormData(BaseModel):
    email: str = None
    password: str = None


    @validator("email")
    @classmethod
    def validate_email(cls, value):
        if "xxx" == value:
            raise FieldError("xxx is an invalid email!")
        return value


@component
def TextInput(label: str, field: FieldModel, props: dict):
    # log.info('TextInput.%s, error=%s', label, field.error)
    log.info('TextInput %s', field)

    props['label'] = label

    return html.p(
        html.label(
            label + ' ',
            html.input(props),
            html.div(field.error)
        )
    )


@component
def AppMain():
    log.info('AppMain')

    form_model, set_model = use_state(LoginFormData(email="jones@gmail.com", password="passme99"))

    Form, Field = createForm(form_model, set_model)
    return Form(
        html.fieldset(
            html.legend("Login"),
            Field('email', lambda field, props: TextInput('Email', field, props({'type':'email'}))),
            Field('password', lambda field, props: TextInput('Password', field, props({'type':'password'})))

        )
    )


# python -m examples.form_login

# Internally app is run by Uvicorn/starlette

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain, host="0.0.0.0", port=8000)