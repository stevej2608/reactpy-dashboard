import pytest
from reactpy import component, html
from reactpy.core.types import VdomChildren
from reactpy.testing import DisplayFixture

from examples.form_complex import AppMain


# pytest -o log_cli=1 --headed tests/test_complex_form.py

@pytest.mark.anyio
async def test_form(display: DisplayFixture):
    await display.show(AppMain)
    assert True
