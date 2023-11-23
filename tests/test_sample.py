import pytest
from reactpy.sample import SampleApp
from tests.page_containers import PicoContainer

@pytest.mark.anyio
async def test_sample_app(pico_container: PicoContainer, page):
    await pico_container.show(SampleApp)
    h1 = await page.wait_for_selector("h1")
    assert (await h1.text_content()) == "Sample Application"
