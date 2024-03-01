from typing import List
from reactpy import component, html
from reactpy.svg import svg, path
from utils.child_list import ChildList

# pylint: disable=line-too-long

@component
def Home():
    return html.li({'class_name': 'inline-flex items-center'},
        html.a({'href': '#', 'class_name': 'inline-flex items-center text-gray-700 hover:text-gray-900'},
            svg({'class_name': 'mr-2.5 h-5 w-5', 'fill': 'currentColor', 'viewbox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
                path({'d': 'M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z'})
            ),
            " Home "
        )
    )


@component
def PathElement(label: str):
    return html.li(
        html.div({'class_name': 'flex items-center'},
            svg({'class_name': 'h-6 w-6 text-gray-400', 'fill': 'currentColor', 'viewbox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
                path({'fill-rule': 'evenodd', 'd': 'M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', 'clip-rule': 'evenodd'})
            ),
            html.a({'href': '#', 'class_name': 'ml-1 text-sm font-medium text-gray-700 hover:text-gray-900 md:ml-2'}, label)
        )
    )


@component
def Breadcrumbs(crumbs: List[str]):

    Route = [PathElement(crumb) for crumb in crumbs]

    return html.nav({'class_name': 'mb-5 flex', 'aria-label': 'Breadcrumb'},
        html.ol({'class_name': 'inline-flex items-center space-x-1 md:space-x-2'},
            Home(),
            ChildList(*Route)
        )
    )