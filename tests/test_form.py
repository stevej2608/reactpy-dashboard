import pytest
from reactpy import component, html
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain

# pytest -o log_cli=1 -sv tests/test_form.py

@pytest.mark.anyio
async def test_form(display: DisplayFixture):

    @component
    def XAppMain():
        props = {'type':'email', 'value': 'littlejoe@gmail.vom'}
        return html.p(
            html.label(
                'Email ',
                html.input(props)
            )
        )

    await display.show(AppMain)

    email_input = display.page.get_by_label("Email")
    assert email_input

    await email_input.fill('bigjoe@gmail.com')
    assert (await email_input.input_value()) == 'bigjoe@gmail.com'
