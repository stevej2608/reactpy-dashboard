from reactpy import component, html

TRANSACTIONS = [
  { 'action': 'Payment from', 'item': 'Bonnie Green', 'date': 'Apr 23 ,2021', 'value': '$2300' },
  { 'action': 'Payment refund to', 'item': '#00910', 'date': 'Apr 23 ,2021', 'value': '-$670' },
  { 'action': 'Payment failed from', 'item': '#087651', 'date': 'Apr 18 ,2021', 'value': '$234' },
  { 'action': 'Payment from', 'item': 'Lana Byrd', 'date': 'Apr 15 ,2021', 'value': '$5000' },
  { 'action': 'Payment from', 'item': 'Jese Leos', 'date': 'Apr 15 ,2021', 'value': '$2300' },
  { 'action': 'Payment from', 'item': 'THEMESBERG LLC', 'date': 'Apr 11 ,2021', 'value': '$560' },
  { 'action': 'Payment from', 'item': 'Lana Lysle', 'date': 'Apr 6 ,2021', 'value': '$1437' }
]

@component
def TableHead():
    return html.thead({'class_name': 'bg-gray-50'},
        html.tr(
            html.th({'scope': 'col', 'class_name': 'p-4 text-left text-xs font-medium uppercase tracking-wider text-gray-500'}, "Transaction"),
            html.th({'scope': 'col', 'class_name': 'p-4 text-left text-xs font-medium uppercase tracking-wider text-gray-500'}, "Date & Time"),
            html.th({'scope': 'col', 'class_name': 'p-4 text-left text-xs font-medium uppercase tracking-wider text-gray-500'}, "Amount")
        )
    )


@component
def TableRow(index, row):
    action, item, date, value = row.values()
    rc = 'bg-gray-50' if index % 2 else ''
    return html.tr({'class_name': rc},
        html.td({'class_name': 'whitespace-nowrap p-4 text-sm font-normal text-gray-900'},
            action + ' ',
            html.span({'class_name': 'font-semibold'}, item)
        ),
        html.td({'class_name': 'whitespace-nowrap p-4 text-sm font-normal text-gray-500'}, date),
        html.td({'class_name': 'whitespace-nowrap p-4 text-sm font-semibold text-gray-900'}, value)
    )

@component
def TableBody():

    table_rows = [TableRow(index, row) for index, row in enumerate(TRANSACTIONS)]

    return html.tbody({'class_name': 'bg-white'},
        table_rows
    )


@component
def TransactionsTable():
    return html.div(
    html.table({'class_name': 'min-w-full divide-y divide-gray-200'},
        TableHead(),
        TableBody()
    )
)
