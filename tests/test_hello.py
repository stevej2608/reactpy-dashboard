import pytest
from reactpy.testing import DisplayFixture
from app_main import MainApp

@pytest.mark.anyio
async def test_sample(display: DisplayFixture):
    await display.show(MainApp)
    h1 = await display.page.wait_for_selector("h1")
    assert (await h1.text_content()) == "Hello, world!"
