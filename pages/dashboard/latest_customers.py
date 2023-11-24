from reactpy import component, html

CUSTOMERS = [
  { 'img_src': '/static/images/users/neil-sims.png', 'name': 'Neil Sims', 'email': 'email@windster.com', 'purchases': '$320' },
  { 'img_src': '/static/images/users/bonnie-green.png', 'name': 'Bonnie Green', 'email': 'email@windster.com', 'purchases': '$3467' },
  { 'img_src': '/static/images/users/michael-gough.png', 'name': 'Michael Gough', 'email': 'email@windster.com', 'purchases': '$67' },
  { 'img_src': '/static/images/users/thomas-lean.png', 'name': 'Thomes Lean', 'email': 'email@windster.com', 'purchases': '$2367' },
  { 'img_src': '/static/images/users/lana-byrd.png', 'name': 'Lana Byrd', 'email': 'email@windster.com', 'purchases': '$367' }
]


def table_row(index, row):

    img_src, name, email, purchases = row.values()

    return html.div({'class_name': 'flow-root', 'key': index},
        html.ul({'role': 'list', 'class_name': 'divide-y divide-gray-200'},
            html.li({'class_name': 'py-3 sm:py-4'},
                html.div({'class_name': 'flex items-center space-x-4'},
                    html.div({'class_name': 'flex-shrink-0'},
                        html.img({'class_name': 'h-8 w-8 rounded-full', 'src': img_src, 'alt': img_src})
                    ),
                    html.div({'class_name': 'min-w-0 flex-1'},
                        html.p({'class_name': 'truncate text-sm font-medium text-gray-900'}, name),
                        html.p({'class_name': 'truncate text-sm text-gray-500'}, email)
                    ),
                    html.div({'class_name': 'inline-flex items-center text-base font-semibold text-gray-900'}, purchases)
                )
            )
        )
    )

@component
def LatestCustomers():

    table_rows = [table_row(index, row) for index, row in enumerate(CUSTOMERS)]


    return html.div({'class_name': 'mb-4 h-full rounded-lg bg-white p-4 shadow sm:p-6'},
        html.div({'class_name': 'mb-4 flex items-center justify-between'},
            html.h3({'class_name': 'text-xl font-bold leading-none text-gray-900'}, "Latest Customers"),
            html.a({'href': '#', 'class_name': 'inline-flex items-center rounded-lg p-2 text-sm font-medium text-cyan-600 hover:bg-gray-100'}, "View all")
        ),
        html.div({'class_name': 'flow-root'},
            html.ul({'role': 'list', 'class_name': 'divide-y divide-gray-200'},
                table_rows
            )
        )
    )
