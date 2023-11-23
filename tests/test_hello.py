import pytest
from examples.hello  import AppMain, GREETING
from tests.page_containers import PicoContainer

@pytest.mark.anyio
async def test_sample(pico_container: PicoContainer, page):
    await pico_container.show(AppMain)
    h2 = await page.wait_for_selector("h2")
    assert (await h2.text_content()) == GREETING
