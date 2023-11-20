import pytest
from reactpy import component, html
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain


def div_field(display, name: str):

    async def wait_for_selector():
        await display.page.wait_for_load_state("networkidle")
        selector = await display.page.wait_for_selector(name)
        return selector

    async def get_text():
        element = await wait_for_selector()
        value = await element.text_content()
        return value

    return get_text


def input_field(display, name: str):

    async def wait_for_selector():
        await display.page.wait_for_load_state("networkidle")
        selector = await display.page.wait_for_selector(name)
        return selector

    async def get_input():
        element = await wait_for_selector()
        value = await element.input_value()
        return value
    
    async def set_input(value):
        element = await wait_for_selector()
        await element.fill(value)

    return [get_input, set_input]


# pytest -o log_cli=1 -sv tests/test_form.py

@pytest.mark.anyio
async def test_form(display: DisplayFixture):

    await display.show(AppMain)

    get_error = div_field(display, '#error')

    get_email, set_email = input_field(display, '#email')
    get_password, set_password = input_field(display, '#password')

    assert (await get_email()) == 'joe@gmail.com'
    assert (await get_password()) == '1234'

    assert (await get_error()) == ''

    await set_email('bigjoe@gmail.com')
    assert (await  get_email()) == 'bigjoe@gmail.com'
    assert (await get_error()) == ''

    await set_email('xxx')
    assert (await  get_email()) == 'xxx'
    assert (await get_error()) == 'xxx is an invalid email!'



