from reactpy import component, html
from reactpy.core.types import VdomChildren
from modules.pico import PICO_CSS

from fast_server import run

@component
def Input(label=None, id=None, type=None, name=None, placeholder=None, value=None):

    input_props = {
        'type': 'search', 
        'id': f'{id}', 
        'name': f'{name}', 
        'placeholder': f'{placeholder}', 
        'value': value
        }

    return html.div(
        html.label({'html_for': f'{id}'}, label ),
        html.input(input_props)     
    )

@component
def Select(options: VdomChildren, name: str = None, label:str = None):
    return html.div(
        html.label({'html_for': name}, label),
        html.select({'id': id, 'name': name, 'required': ''},
            options
        )
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


        html.label({'html_for': 'select'}, "Select"),
        html.select({'id': 'select', 'name': 'select', 'required': ''},
            html.option({'value': '', 'selected': ''}, "Select…"),
            html.option("…")
        ),
        # File browser,
        html.label({'html_for': 'file'},
            "File browser",
            html.input({'type': 'file', 'id': 'file', 'name': 'file'})
        ),
        # Range slider control,
        html.label({'html_for': 'range'},
            "Range slider",
            html.input({'type': 'range', 'min': '0', 'max': '100', 'value': '50', 'id': 'range', 'name': 'range'})
        ),
        # States,
        html.div({'class_name': 'grid'},
            html.label({'html_for': 'valid'},
                "Valid",
                html.input({'type': 'text', 'id': 'valid', 'name': 'valid', 'placeholder': 'Valid', 'aria-invalid': 'false'})
            ),
            html.label({'html_for': 'invalid'},
                "Invalid",
                html.input({'type': 'text', 'id': 'invalid', 'name': 'invalid', 'placeholder': 'Invalid', 'aria-invalid': 'true'})
            ),
            html.label({'html_for': 'disabled'},
                "Disabled",
                html.input({'type': 'text', 'id': 'disabled', 'name': 'disabled', 'placeholder': 'Disabled', 'disabled': ''})
            )
        ),
        html.div({'class_name': 'grid'},
            # Date,
            html.label({'html_for': 'date'},
                "Date",
                html.input({'type': 'date', 'id': 'date', 'name': 'date'})
            ),
            # Time,
            html.label({'html_for': 'time'},
                "Time",
                html.input({'type': 'time', 'id': 'time', 'name': 'time'})
            ),
            # Color,
            html.label({'html_for': 'color'},
                "Color",
                html.input({'type': 'color', 'id': 'color', 'name': 'color', 'value': '#0eaaaa'})
            )
        ),
        html.div({'class_name': 'grid'},
            # Checkboxes,
            html.fieldset(
                html.legend(
                    html.strong("Checkboxes")
                ),
                html.label({'html_for': 'checkbox-1'},
                    html.input({'type': 'checkbox', 'id': 'checkbox-1', 'name': 'checkbox-1', 'checked': ''}),
                    "Checkbox"
                ),
                html.label({'html_for': 'checkbox-2'},
                    html.input({'type': 'checkbox', 'id': 'checkbox-2', 'name': 'checkbox-2'}),
                    "Checkbox"
                )
            ),
            # Radio buttons,
            html.fieldset(
                html.legend(
                    html.strong("Radio buttons")
                ),
                html.label({'html_for': 'radio-1'},
                    html.input({'type': 'radio', 'id': 'radio-1', 'name': 'radio', 'value': 'radio-1', 'checked': ''}),
                    "Radio button"
                ),
                html.label({'html_for': 'radio-2'},
                    html.input({'type': 'radio', 'id': 'radio-2', 'name': 'radio', 'value': 'radio-2'}),
                    "Radio button"
                )
            ),
            # Switch,
            html.fieldset(
                html.legend(
                    html.strong("Switches")
                ),
                html.label({'html_for': 'switch-1'},
                    html.input({'type': 'checkbox', 'id': 'switch-1', 'name': 'switch-1', 'role': 'switch', 'checked': ''}),
                    "Switch"
                ),
                html.label({'html_for': 'switch-2'},
                    html.input({'type': 'checkbox', 'id': 'switch-2', 'name': 'switch-2', 'role': 'switch'}),
                    "Switch"
                )
            )
        ),
        # Buttons,
        html.input({'type': 'reset', 'value': 'Reset', 'onclick': 'event.preventDefault()'}),
        html.input({'type': 'submit', 'value': 'Submit', 'onclick': 'event.preventDefault()'})
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
