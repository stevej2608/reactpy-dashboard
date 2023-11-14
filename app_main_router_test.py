from reactpy import Ref, component, html
from reactpy.svg import svg, path
from reactpy_router import link, route, simple
from utils.logger import log, logging
from pages.components.icon import Icon_Dashboard

from fast_server import run

# reactpy_router/tests/test_core.py

render_count = Ref(0)

@component
def SimpleButton(text:str):
    """This works"""
    return html.div(text)
    # return html.div(text, Icon_Dashboard())


@component
def SideBarItem(text, icon):
    return html.div({'class_name': 'group flex items-center rounded-lg p-2 text-base font-normal text-gray-900 hover:bg-gray-100'},

        svg({'class_name': 'h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
                path({'d': 'M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z'}),
                path({'d': 'M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z'})
            ),

        html.span({'class_name': 'ml-3 flex-1 whitespace-nowrap'}, text)
    )

@component
def AppMain():
    render_count.current += 1
    log.info('****************** AppMain render_count=%d ********************', render_count.current)

    @component
    def root():
        log.info("[Root]")
        return html.div(
            html.h2('ROOT XX'),
            # link(SimpleButton("[Page A  YY]"), to="/a", id="root"),
            # SideBarItem("Page A XX", icon=Icon_Dashboard),
            link(SideBarItem("Page A SB", icon=Icon_Dashboard), to="/a", id="XXX")
            # SideBarItem("Page A", icon=Icon_Dashboard, to="/a")
        )

    @component
    def page_a():
        log.info("[Page A]")
        return html.div(
            html.h2('Page A'),
            link("[Home]", to="/", id="a")
        )

    return simple.router(
        route("/", root()),
        route("/a", page_a()),
        # route("/b", page_b()),
        # route("/c", page_c()),
        # route("*", page_404()),
    )

# python app_main_router_test.py
#
# Internally app is run by Uvicorn/starlette
#

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    log.info('Starting...')
    run(AppMain, host="0.0.0.0", port=8000)
