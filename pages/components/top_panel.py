from reactpy import component, html
from reactpy.core.types import VdomChildren
from utils.child_list import ChildList


@component
def TopPanel(*children: VdomChildren):

    return html.div({'class_name': 'block items-center justify-between border-gray-200 bg-white p-4 sm:flex lg:mt-1.5'},
        html.div({'class_name': 'mb-1 w-full'},
            ChildList(*children)
        )
    )
