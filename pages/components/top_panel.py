from reactpy import component, html
from reactpy.core.types import VdomChildren
from utils.child_list import ChildList


@component
def TopPanel(*children: VdomChildren):

    for index, child in enumerate(children):
        child.key = index

    return html.div({'class_name': 'block items-center justify-between border-b border-gray-200 bg-white p-4 sm:flex lg:mt-1.5'},
        html.div({'class_name': 'mb-1 w-full'},
            html.div({'class_name': 'mb-4'},
                ChildList(*children)
            )
        )
    )
