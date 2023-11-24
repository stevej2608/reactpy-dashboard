from reactpy import component, html

ACQUISITIONS = [
  { 'channels': 'Organic Search', 'users': '5,649', 'performance': '30%', 'color': 'bg-cyan-600' },
  { 'channels': 'Referral', 'users': '4,025', 'performance': '24%', 'color': 'bg-orange-300' },
  { 'channels': 'Direct', 'users': '3,105', 'performance': '18%', 'color': 'bg-teal-400' },
  { 'channels': 'Social', 'users': '1251', 'performance': '12%', 'color': 'bg-pink-600' },
  { 'channels': 'Other', 'users': '734', 'performance': '9%', 'color': 'bg-indigo-600' },
  { 'channels': 'Email', 'users': '456', 'performance': '7%', 'color': 'bg-purple-500' }
]


@component
def TableHead():
    return html.thead(
        html.tr(
            html.th({'class_name': 'whitespace-nowrap border-l-0 border-r-0 bg-gray-50 px-4 py-3 text-left align-middle text-xs font-semibold uppercase text-gray-700'}, "Top Channels"),
            html.th({'class_name': 'whitespace-nowrap border-l-0 border-r-0 bg-gray-50 px-4 py-3 text-left align-middle text-xs font-semibold uppercase text-gray-700'}, "Users"),
            html.th({'class_name': 'min-w-140-px whitespace-nowrap border-l-0 border-r-0 bg-gray-50 px-4 py-3 text-left align-middle text-xs font-semibold uppercase text-gray-700'})
        )
    )


def table_row(index, row):

    channels, users, performance, color = row.values()

    style = f"width: {performance}"
    bar_class = f"{color} h-2 rounded-sm"


    return html.tr({'class_name': 'text-gray-500', 'key': index},
        html.th({'class_name': 'whitespace-nowrap border-t-0 p-4 px-4 text-left align-middle text-sm font-normal'}, channels),
        html.td({'class_name': 'whitespace-nowrap border-t-0 p-4 px-4 align-middle text-xs font-medium text-gray-900'}, users),
        html.td({'class_name': 'whitespace-nowrap border-t-0 p-4 px-4 align-middle text-xs'},
            html.div({'class_name': 'flex items-center'},
                html.span({'class_name': 'mr-2 text-xs font-medium'}, performance),
                html.div({'class_name': 'relative w-full'},
                    html.div({'class_name': 'h-2 w-full rounded-sm bg-gray-200'},
                        html.div({'class_name': bar_class, 'style': style})
                    )
                )
            )
        )
    )



@component
def TableBody():

    table_rows = [table_row(index, row) for index, row in enumerate(ACQUISITIONS)]

    return html.tbody({'class_name': 'divide-y divide-gray-100'},
        table_rows
    )

@component
def AcquisitionOverview():
    return html.div({'class_name': 'rounded-lg bg-white p-4 shadow sm:p-6 xl:p-8'},
        html.h3({'class_name': 'mb-10 text-xl font-bold leading-none text-gray-900'}, "Acquisition Overview"),
        html.div({'class_name': 'block w-full overflow-x-auto'},
            html.table({'class_name': 'w-full border-collapse items-center bg-transparent'},
                TableHead(),
                TableBody()
            )
        )
    )
