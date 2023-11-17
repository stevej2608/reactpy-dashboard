from reactpy import component, html, run

@component
def AppMain():
    return html.form(
        html.fieldset(
            html.legend("Personal Details"),
            html.p(
                html.label(
                    "Salutation",
                    html.br(),
                    html.select({'name': 'salutation'},
                        html.option("--None--"),
                        html.option("Mr."),
                        html.option("Ms."),
                        html.option("Mrs."),
                        html.option("Dr."),
                        html.option("Prof.")
                    )
                )
            ),
            html.p(
                html.label(
                    "First name:",
                    html.input({'name': 'firstName'})
                )
            ),
            html.p(
                html.label(
                    "Last name:",
                    html.input({'name': 'lastName'})
                )
            ),
            html.p(
                "Gender :",
                html.label(
                    html.input({'type': 'radio', 'name': 'gender', 'value': 'male'}),
                    "Male"
                ),
                html.label(
                    html.input({'type': 'radio', 'name': 'gender', 'value': 'female'}),
                    "Female"
                )
            ),
            html.p(
                html.label(
                    "Email:",
                    html.input({'type': 'email', 'name': 'email'})
                )
            ),
            html.p(
                html.label(
                    "Date of Birth:",
                    html.input({'type': 'date', 'name': 'birthDate'})
                )
            ),
            html.p(
                html.label(
                    "Address :",
                    html.br(),
                    html.textarea({'name': 'address', 'cols': '30', 'rows': '3'})
                )
            ),
            html.p(
                html.button({'type': 'submit'}, "Submit")
            )
        )
    )

# python examples/form_complex.py

# Internally app is run by Uvicorn/starlette


if __name__ == "__main__":
    run(AppMain, host="0.0.0.0", port=8000)
