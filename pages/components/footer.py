from reactpy import component, html

@component
def Footer():
    return html.footer({'class_name': 'mx-4 my-6 rounded-lg bg-white p-4 shadow md:flex md:items-center md:justify-between md:p-6 xl:p-8'},
        html.ul({'class_name': 'mb-6 flex flex-wrap items-center md:mb-0'},
            html.li(
                html.a({'href': '#', 'class_name': 'mr-4 text-sm font-normal text-gray-500 hover:underline md:mr-6'}, "Terms and conditions")
            ),
            html.li(
                html.a({'href': '#', 'class_name': 'mr-4 text-sm font-normal text-gray-500 hover:underline md:mr-6'}, "Privacy Policy")
            ),
            html.li(
                html.a({'href': '#', 'class_name': 'mr-4 text-sm font-normal text-gray-500 hover:underline md:mr-6'}, "Licensing")
            ),
            html.li(
                html.a({'href': '#', 'class_name': 'mr-4 text-sm font-normal text-gray-500 hover:underline md:mr-6'}, "Cookie Policy")
            ),
            html.li(
                html.a({'href': '#', 'class_name': 'text-sm font-normal text-gray-500 hover:underline'}, "Contact")
            )
        )
    )
