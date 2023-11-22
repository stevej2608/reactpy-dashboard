from utils.props import props


def test_simple():

    def Input(label:str=None, id:str=None, name:str=None, placeholder:str=None, value:str=None):
        _props = props(include="id, name, placeholder, value")
        return _props

    result = Input(id='search', name='search', placeholder='Search', label='Search', value='')

    assert result == {'id': 'search', 'name': 'search', 'placeholder': 'Search', 'value': ''}
