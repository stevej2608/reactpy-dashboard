from typing import Literal
from reactpy import component, html
from reactpy.core.types import VdomChildren
from utils.props import props

InputTypes = Literal[
    'button'
    'checkbox',
    'date',
    'datetime-local',
    'email',
    'file',
    'image',
    'month',
    'number',
    'password',
    'radio',
    'reset',
    'search',
    'submit',
    'tel',
    'text', 
    'time',
    'url',
    'week', 
]


@component
def Input(label:str='', id:str=None, type:InputTypes='text',
          name:str=None, placeholder:str=None, value:str=None, role:str=None,
          invalid:bool=None, disabled:bool=None):

    input_props = props(include='id, type, name, placeholder, role, value, disabled')

    if invalid is not None:
        input_props['aria-invalid'] = invalid

    if type in ['checkbox', 'radio']:
        return html.div(
            html.input(input_props),
            html.label({'html_for': id}, label )
        )

    return html.div(
        html.label({'html_for': id}, label ),
        html.input(input_props)
    )

@component
def RangeSlider(min:int=0, max:int=100, value:int=0, id:str=None, name:str=None, label:str=None):
    input_props = {'type': 'range', **props(include="min, max, value, id, name")}
    return html.div(
        html.label({'html_for': id}, label ),
        html.input(input_props)
    )

@component
def Select(options: VdomChildren, name:str='', label:str=''):
    return html.div(
        html.label({'html_for': id}, label),
        html.select({'id': id, 'name': name, 'required': ''},
            options
        )
    )

@component
def FieldSet(legend:str=None, children: VdomChildren = None):
    return html.fieldset(
        html.legend(html.strong(legend)),
        children
    )
