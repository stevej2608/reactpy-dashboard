
from reactpy import component, html, use_context, use_location
from reactpy.core.types import VdomDictConstructor
from reactpy.types import VdomChildren

from utils.logger import log

from .components.app_store import AppContext
from .components.side_bar import SideBar
from .components.top_bar import TopBar


@component
def PageContainer(page: VdomDictConstructor):
    context, _ = use_context(AppContext)

    log.info("PageContainer.render() location %s", use_location())

    @component
    def RightHandPanel(children: VdomChildren):
        visible = 'ml-64' if context.sidebar_open else 'ml-0'
        return html.div({'class_name': f'flex-1 flex flex-col min-h-screen pt-16 transition-[margin] duration-200 ease-in-out {visible}'},
            children
         )


    return html.div({'class_name': 'min-h-full w-full'},
        html.div({'class_name': 'min-h-screen flex flex-col bg-white'},
            TopBar(),
            SideBar(),
            RightHandPanel(
                page(),
            )
        )
    )