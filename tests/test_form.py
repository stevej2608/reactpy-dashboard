import pytest
from reactpy import component, html
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain

class Selector:

    @property
    async def selector(self):
        await self._page.wait_for_load_state("networkidle")
        element = await self._page.wait_for_selector(self._selector)
        return element

    def __init__(self, display, sel):
        self._page = display.page
        self._selector = sel


# pytest -o log_cli=1 -sv tests/test_form.py

@pytest.mark.anyio
async def test_form(display: DisplayFixture):

    await display.show(AppMain)

    async def wait_for_selector(selector):
        await display.page.wait_for_load_state("networkidle")
        selector = await display.page.wait_for_selector(selector)
        return selector

    async def get_input(selector):
        element = await wait_for_selector(selector)
        value = await element.input_value()
        return value

    async def set_input(selector, value):
        element = await wait_for_selector(selector)
        await element.fill(value)

    assert (await get_input("#email")) == 'joe@gmail.com'

    await set_input("#email", 'bigjoe@gmail.com')
    assert (await get_input("#email")) == 'bigjoe@gmail.com'

    await set_input("#email", 'xxx')
    assert (await get_input("#email")) == 'xxx'



