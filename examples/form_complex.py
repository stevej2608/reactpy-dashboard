from typing import Literal
from reactpy import component, html
from reactpy.core.types import VdomChildren
from modules.pico import PICO_CSS
from utils.props import props

from fast_server import run

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



@component
def ComplexForm():
    return html.form(
        html.h2("Form elements"),
        # Search,
        Input(type='search', id='search', name='search', placeholder='Search', label='Search', value=''),

        # Text,
        Input(type='text', id='text', name='text', placeholder='Text', label='Text', value=''),
        html.small("Curabitur consequat lacus at lacus porta finibus."),

        # Select,

        Select(
            html._(
                html.option({'value': '', 'selected': ''}, "Select…"),
                html.option("…")
            ),
            name='select', label = 'Select'
        ),

        # File browser,

        Input(type='file', id='file', name='file',label='File browser', value=''),

        # Range slider control,

        RangeSlider(min=0, max=100, value=50, id='range', name='range', label='Range Slider'),

        # States,
        html.div({'class_name': 'grid'},
            Input(type='text', id='valid', name='valid', placeholder='valid', label='Valid', invalid=False),
            Input(type='text', id='invalid', name='invalid', placeholder='invalid', label='Invalid', invalid=True),
            Input(type='text', id='disabled', name='disabled',placeholder='disabled' ,label='Disabled', disabled=True),

        ),
        html.div({'class_name': 'grid'},
            # Date,
            Input(type='date', id='date', name='date', label='Date'),
            # Time
            Input(type='time', id='time', name='time', label='Time'),
            # Color
            Input(type='color', id='color', name='color', label='Color')

        ),
        html.div({'class_name': 'grid'},
            # Checkboxes,
            FieldSet(legend='Checkboxes',
                children=html._(
                    Input(type='checkbox', id='checkbox-1', name='checkbox-1', label='Checkbox'),
                    Input(type='checkbox', id='checkbox-2', name='checkbox-2', label='Checkbox')
                )
            ),

            # Radio buttons,

            FieldSet(legend='Radio buttons',
                children=html._(
                    Input(type='radio', id='radio-1', name='radio-1', label='Radio'),
                    Input(type='radio', id='radio-2', name='radio-2', label='Radio')
                )
            ),


            # Switch,

            FieldSet(legend='Switches',
                children=html._(
                    Input(type='checkbox', id='switch-1', name='switch-1', role='switch', label='Switch'),
                    Input(type='checkbox', id='switch-2', name='switch-2', role='switch', label='Switch')
                )
            ),

        ),
        # Buttons,
        Input(type='reset', value='Reset'),
        Input(type='submit', value='Submit')
    )



@component
def AppMain():
    return html._(
        html.head(
            html.link(PICO_CSS)
        ),
        html.main({'class_name': 'container'},
            html.section(
                ComplexForm()
            )
        )
    )

# python -m examples.form_complex

# Internally app is run by Uvicorn/starlette

if __name__ == "__main__":
    run(AppMain)
