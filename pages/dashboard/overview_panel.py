from reactpy import component, html

from ..components.icon import Icon_DownArrow, Icon_UpArrow

@component
def OverviewPanel(title, number, change):

    up = not change.startswith('-')
    ArrowIcon = Icon_UpArrow if up else Icon_DownArrow
    colour = 'text-green-500' if up  else 'text-red-500'
    div_class = f"ml-5 w-0 flex items-center justify-end flex-1 {colour} text-base font-bold"


    return html.div(
    html.div({'class_name': 'rounded-lg bg-white p-4 shadow sm:p-6 xl:p-8'},
        html.div({'class_name': 'flex items-center'},
            html.div({'class_name': 'flex-shrink-0'},
                html.span({'class_name': 'text-2xl font-bold leading-none text-gray-900 sm:text-3xl'}, number),
                html.h3({'class_name': 'text-base font-normal text-gray-500'}, title)
            ),
            html.div({'class_name': div_class},
                change,
                ArrowIcon()
            )
        )
    )
)
