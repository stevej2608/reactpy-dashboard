from reactpy import component, html
from reactpy.types import VdomChildren

# ./solidjs-dashboard/src/components/DarkModeProvider.tsx

@component
def DarkModeProvider(dark_mode: bool, children: VdomChildren):
    dark = 'dark' if dark_mode else 'light'
    return html.div({'class_name': dark}, children)
