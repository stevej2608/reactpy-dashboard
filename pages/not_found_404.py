from reactpy import component, html
from reactpy_router import link
from .components.button import ButtonWithIcon
from .components.icon import ICON

# https://demo.themesberg.com/volt/pages/examples/404.html

@component
def NotFoundPage():
    return html.div({'class_name': 'pt:mt-0 mx-auto flex flex-col items-center justify-center px-6 pt-8 md:h-screen'},
        html.div({'class_name': 'row'},
            html.div({'class_name': 'col-12 text-center d-flex align-items-center justify-content-center'},
                html.div(
                    html.img({'alt': '404 not found', 'class_name': 'img-fluid w-75', 'src': 'static/images/404.svg'}),
                    html.h1({'class_name': 'text-4xl font-bold mt-5'},"Page not found"),
                    html.p({'class_name': 'text-xl  m-5'}, "Oops! Looks like you followed a bad link. If you think this is a problem with us, please tell us."),
                    link({'to': '/'}, ButtonWithIcon("Back to homepage", ICON.BackArrow))
                )
            )
        )
    )
