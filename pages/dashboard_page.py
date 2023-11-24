from reactpy import component, html

from .dashboard.transactions_table import TransactionsTable
from .dashboard.sales_chart import SalesChart
from .dashboard.overview_panel import OverviewPanel
from .dashboard.latest_customers import LatestCustomers
from .dashboard.acquisition_overview import AcquisitionOverview

from .components.icon import Icon_UpArrow


@component
def TopRow():
    return html.div({'class_name': 'grid w-full grid-cols-1 gap-4 xl:grid-cols-2 2xl:grid-cols-3'},
        # Sales this week,
        html.div({'class_name': 'rounded-lg bg-white p-4 shadow sm:p-6 xl:p-8 2xl:col-span-2'},
            html.div({'class_name': 'mb-4 flex items-center justify-between'},
                html.div({'class_name': 'flex-shrink-0'},
                    html.span({'class_name': 'text-2xl font-bold leading-none text-gray-900 sm:text-3xl'}, "$45,385"),
                    html.h3({'class_name': 'text-base font-normal text-gray-500'}, "Sales this week")
                ),
                html.div({'class_name': 'flex flex-1 items-center justify-end text-base font-bold text-green-500'},
                    "12.5%",
                    Icon_UpArrow()
                )
            ),
            html.div({'id': 'main-chart', 'style': 'min-height: 435px;'},
                SalesChart()
            )
        ),

        # Latest Transactions

        html.div({'class_name': 'rounded-lg bg-white p-4 shadow sm:p-6 xl:p-8'},
            html.div({'class_name': 'mb-4 flex items-center justify-between'},
                html.div(
                    html.h3({'class_name': 'mb-2 text-xl font-bold text-gray-900'}, "Latest Transactions"),
                    html.span({'class_name': 'text-base font-normal text-gray-500'}, "This is a list of latest transactions")
                ),
                html.div({'class_name': 'flex-shrink-0'},
                    html.a({'href': '#', 'class_name': 'rounded-lg p-2 text-sm font-medium text-cyan-600 hover:bg-gray-100'}, "View all")
                )
            ),
            html.div({'class_name': 'mt-8 flex flex-col'},
                html.div({'class_name': 'overflow-x-auto rounded-lg'},
                    TransactionsTable()
                )
            )
        )
    )


@component
def MiddleRow():
    return html.div({'class_name': 'mt-4 grid w-full grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-3'},
        OverviewPanel(title="New products this week", number=2340, change="14.6%"),
        OverviewPanel(title="Visitors this week", number=5355, change="32.9%"),
        OverviewPanel(title="User signups this week", number=385, change="-2.7%")
    )


@component
def BottomRow():
    return html.div({'class_name': 'my-4 grid grid-cols-1 xl:gap-4 2xl:grid-cols-2'},
        LatestCustomers(),
        # AcquisitionOverview()
    )


@component
def Dashboard():
    return html.main(
        html.div({'class_name': 'px-4 pt-6'},
            TopRow(),
            MiddleRow(),
            BottomRow()
        )
    )

