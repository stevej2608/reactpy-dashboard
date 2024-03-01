from reactpy import component, html

@component
def Logo():
    return html.a({'href': '/', 'class_name': 'flex items-center text-xl font-bold lg:ml-2.5'},
        html.img({'src': '/static/images/logo.svg', 'class_name': 'mr-2 h-6', 'alt': 'React/Py Logo'}),
        html.span({'class_name': 'self-center whitespace-nowrap'}, "React/Py")
    )
