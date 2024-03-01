from typing import Any, Dict, Union, List
from reactpy import component, html


def clsx(*argv: List[Union[Any, Dict[Any, Any]]]) -> Dict[Any, Any]:
    result: Dict[Any, Any] = {}
    for d in argv:
        if isinstance(d, dict):
            result.update(d)
    return result

@component
def Input(attributes: Dict[str, Any], **argc: Any):

    attributes['class_name'] = ' '.join([
        'bg-gray-50 border border-gray-300 text-gray-900 outline-none focus:outline-none sm:text-sm rounded-lg focus:border-cyan-600 block w-full p-2.5',
        attributes.pop('class_name', '')
    ])


    return html.input(attributes, **argc)


@component
def Label(label: str):
    return html.label({'class_name': 'mb-2 block text-sm font-medium text-gray-900'}, label)


@component
def TextInput(label: str, props: Dict[str, Any]):
    return html.div({'class_name': 'border-0'},
        Label(label),
        Input(props)
    )
