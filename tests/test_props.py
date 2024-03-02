from typing import Optional
from utils.props import props


def test_simple():
    def Input(
        label: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        placeholder: Optional[str] = None,
        value: Optional[str] = None,
    ):
        _props = props(include="id, name, placeholder, value")
        return _props

    result = Input(id="search", name="search", placeholder="Search", label="Search", value="")

    assert result == {"id": "search", "name": "search", "placeholder": "Search", "value": ""}
