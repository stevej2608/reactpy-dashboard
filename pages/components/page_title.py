from reactpy import component, html

@component
def PageTitle(title:str):
    return html.h1({'class_name': 'text-xl font-semibold text-gray-900 sm:text-2xl'}, title)
