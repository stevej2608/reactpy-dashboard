import pytest
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain

@pytest.mark.anyio
async def test_sample(display: DisplayFixture):
    await display.show(AppMain)
    form = await display.page.wait_for_selector("form")
    assert form
