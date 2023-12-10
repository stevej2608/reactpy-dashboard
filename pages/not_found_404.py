from reactpy import component, html
from reactpy_router import link
from .components.icon import Icon_BackArrow, Icon_Gear


@component
def NotFoundPage():


    @component
    def Button(text, icon):
        icon = icon().type()
        return html.div({'class_name': 'w-1/2 text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-4 focus:ring-cyan-200 font-medium inline-flex items-center justify-center rounded-lg text-sm px-3 py-2 text-center sm:w-auto'},
            icon,
            text)


    return html.div({'class_name': 'pt:mt-0 mx-auto flex flex-col items-center justify-center px-6 pt-8 md:h-screen'},
        html.div({'class_name': 'row'},
            html.div({'class_name': 'col-12 text-center d-flex align-items-center justify-content-center'},
                html.div(
                    html.img({'alt': '404 not found', 'class_name': 'img-fluid w-75', 'src': 'static/images/404.svg'}),
                    html.h1({'class_name': 'text-4xl font-bold mt-5'},"Page not found"),
                    html.p({'class_name': 'text-xl  m-5'}, "Oops! Looks like you followed a bad link. If you think this is a problem with us, please tell us."),
                    link(Button("Back to homepage", Icon_BackArrow), to='/products')
                )
            )
        )
    )
