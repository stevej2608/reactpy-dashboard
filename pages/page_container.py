
from reactpy import component, html
from reactpy.core.types import VdomDictConstructor

from utils.types import Props

from .components.mobile_logic import SideBarBackdrop
from .components.side_bar import SideBar
from .components.top_bar import TopBar


@component
def PageContainer(page: VdomDictConstructor, **props: Props):
    return html.div(
        TopBar(),
        html.div({'class_name': 'flex overflow-hidden bg-white pt-16'},
            SideBar(),
            SideBarBackdrop(),
            html.div({'id': 'main-content', 'class_name': 'relative h-full w-full overflow-y-auto bg-gray-50 lg:ml-64'},
                page(**props),
            )
        )

    )
