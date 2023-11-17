from reactpy import component, html, run

@component
def AppMain():
    return html.form(
        html.fieldset(
            html.legend("Login"),
            html.p(
                html.label(
                    "email:",
                    html.input({'email': 'email'})
                )
            ),
            html.p(
                html.label(
                    "password:",
                    html.input({'name': 'password'})
                )
            ),
            html.p(
                html.button({'type': 'submit'}, "Submit")
            )
        )
    )

# python examples/form_login.py

# Internally app is run by Uvicorn/starlette


if __name__ == "__main__":
    run(AppMain, host="0.0.0.0", port=8000)
