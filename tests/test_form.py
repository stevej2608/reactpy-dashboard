import pytest
from reactpy.testing import DisplayFixture

from examples.form_login import AppMain

@pytest.mark.anyio
async def test_sample(display: DisplayFixture):
    await display.show(AppMain)
    form = await display.page.get_by_label("email")
    await form.fill('bigjoe@gmail.com')
    assert form
