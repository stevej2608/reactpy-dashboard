from reactpy import component, html

@component
def DarkModeProvider(provider, children):
    return html.div({'class_name': 'light'}, children)
