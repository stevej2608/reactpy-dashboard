import pytest
from playwright.async_api._generated import Page
from reactpy.sample import SampleApp
from tests.page_containers import PicoContainer

@pytest.mark.anyio
async def test_table(pico_container: PicoContainer, page: Page):
    await pico_container.show(SampleApp)

    h1 = await page.wait_for_selector("h1")

    assert h1
    assert (await h1.text_content()) == "Sample Application"
