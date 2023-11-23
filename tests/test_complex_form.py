import pytest
from examples.form_complex import ComplexForm
from tests.page_containers import PicoContainer

# pytest -o log_cli=1 --headed tests/test_complex_form.py

@pytest.mark.anyio
async def test_form(pico_container: PicoContainer):
    await pico_container.show(ComplexForm)
    assert True
