from reactpy import component, html

# ./solidjs-dashboard/src/components/DarkModeProvider.tsx

@component
def DarkModeProvider(dark_mode: bool, children):
    dark = 'dark' if dark_mode else 'light'
    return html.div({'class_name': dark}, children)
