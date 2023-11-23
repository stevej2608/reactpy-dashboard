import pytest
from examples.form_complex import ComplexForm


# pytest -o log_cli=1 --headed tests/test_complex_form.py

@pytest.mark.anyio
async def test_form(pico_container):
    await pico_container.show(ComplexForm)
    assert True
