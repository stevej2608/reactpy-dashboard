import pytest
from reactpy.testing import DisplayFixture
from app_main import AppMain, GREETING

@pytest.mark.anyio
async def test_sample(display: DisplayFixture):
    await display.show(AppMain)
    h2 = await display.page.wait_for_selector("h2")
    assert (await h2.text_content()) == GREETING
