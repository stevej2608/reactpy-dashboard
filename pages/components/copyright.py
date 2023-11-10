from reactpy import component, html

@component
def Copyright():
    return html.p({'class_name': 'my-10 text-center text-sm text-gray-500'},
        "© 2019-2021" + " ",
        html.a({'href': 'https://themesberg.com', 'class_name': 'hover:underline', 'target': '_blank'}, "Themesberg"),
        ". All rights reserved."
    )

