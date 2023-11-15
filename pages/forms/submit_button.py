from reactpy import component, html

@component
def SubmitButton(label):
    return html.button(
        {'type': 'submit', 'class_name': 'w-full rounded-lg bg-cyan-600 px-5 py-3 text-center text-base font-medium text-white hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200 sm:w-auto'},
        label
        )
