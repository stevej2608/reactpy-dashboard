import pytest
from reactpy import component, html
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain


def error_field(page, name: str):

    async def get_text():
        element = await page.query_selector(name)
        value = await element.text_content()
        return value

    return get_text


def input_field(page, name: str):

    async def get_input():
        element = await page.query_selector(name)
        value = await element.input_value()
        return value
    
    async def set_input(value):
        element = await page.query_selector(name)
        await element.fill(value)
        await page.wait_page_stable()

    return [get_input, set_input]


# pytest -o log_cli=1 --headed tests/test_form.py

@pytest.mark.anyio
async def test_form(display: DisplayFixture, page):

    await display.show(AppMain)

    get_error = error_field(page, '#email-error')

    get_email, set_email = input_field(page, '#email')
    get_password, set_password = input_field(page, '#password')

    # Test initial condition

    assert (await get_email()) == 'joe@gmail.com'
    assert (await get_password()) == '1234'
    assert (await get_error()) == ''

    # Add valid email

    await set_email('bigjoe@gmail.com')
    assert (await  get_email()) == 'bigjoe@gmail.com'
    assert (await get_error()) == ''

    # Add invalid email - test for error message

    await set_email('xxx')
    assert (await  get_email()) == 'xxx'
    assert (await get_error()) == 'xxx is an invalid email!'

    # Add valid email

    await set_email('bigjoe@gmail.com')
    assert (await  get_email()) == 'bigjoe@gmail.com'
    assert (await get_error()) == ''



