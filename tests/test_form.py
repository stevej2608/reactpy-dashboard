import pytest
from reactpy import component, html
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain

# pytest -o log_cli=1 -sv tests/test_form.py

@pytest.mark.anyio
async def test_form(display: DisplayFixture):

    await display.show(AppMain)

    async def wait_for_selector(selector):
        selector = await display.page.wait_for_selector(selector)
        return selector
    
    async def wait_for_input(selector):
        selector = await wait_for_selector(selector)
        value = await selector.input_value()
        return value

    email_input = await wait_for_selector("#email")
    await email_input.fill('bigjoe@gmail.com')

    email_input = await wait_for_selector("#email")
    assert (await email_input.input_value()) == 'bigjoe@gmail.com'


    email_input = await wait_for_selector("#email")
    await email_input.fill('xxx')

    email_input = await wait_for_selector("#email")
    assert (await email_input.input_value()) == 'xxx'

