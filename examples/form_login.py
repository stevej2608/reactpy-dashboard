from pydantic import BaseModel
from reactpy import component, html, run

from utils.logger import log, logging
from reactpy_forms import createForm

class LoginFormData(BaseModel):
    email: str
    password: str

@component
def AppMain():

    log.info('AppMain')

    Form, Field, _ = createForm(LoginFormData)
    return Form(
        html.fieldset(
            html.legend("Login"),
            html.p(
                html.label(
                    "email:",
                    Field('email', lambda field, props: html.input(props({'type':'email'})))
                )
            ),
            html.p(
                html.label(
                    "password:",
                    Field('password', lambda field, props: html.input(props({'type':'password'})))
                )
            ),
        )
    )


# python -m examples.form_login

# Internally app is run by Uvicorn/starlette

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain, host="0.0.0.0", port=8000)
