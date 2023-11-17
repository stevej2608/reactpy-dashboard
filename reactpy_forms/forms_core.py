from pydantic import BaseModel
from typing import Tuple, Callable, TypeVar, List, Any
from reactpy import html
from reactpy.core.component import Component

from utils.logger import log

# Loosly based on modularforms:
#       https://modularforms.dev/solid/guides/create-your-form


# https://modularforms.dev/solid/guides/define-your-form
# ComponentLambda = Callable[[Field, dict], Component]
# def Field(name:str, component_lambda: Callable[[Field, dict], Component]) -> Component:
#     return component_lambda()


Field = Callable[[str,Callable], Component]
Form = Callable[[*List[Component]], Component]

def createForm(form: BaseModel) -> Tuple[Form, Field, List[Field]]:
    """
    
    The returned Form, Field and FieldArray component are connected with the store of 
    your form. They are aware of your fields and their data types, which 
    gives you the benefit of type safety and autocompletion

    Args:
        form (BaseModel): _description_

    Returns:
        Tuple[str, Component, float]: _description_
    """

    log.info('createForm')

    _field_list = []

    _field = None


    def _field(name, fn) -> Component:

        log.info('_field %s', name)

        def onchange(event):
            log.info('%s.onchange(value=%s)', name, event['currentTarget']['value'])

        def _props(props):
            log.info('_props %s', name)
            props['name'] = name
            props['onchange'] = onchange
            return props

        form_input = fn(_field, _props)
        return form_input

    def _form(*fields: List[Component]):
        # form_elements = []
        # attributes = {}
        # for field in fields:
        #     form_elements += [field(attributes)]
        # return html.form(*form_elements)
        return html.form(*fields)

    return [_form, _field, _field_list]
