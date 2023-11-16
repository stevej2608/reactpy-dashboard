from reactpy import component, html
from reactpy.core.component import Component
from reactpy_router import link

@component
def StandardFormContainer(title:str, form: Component):
    return html.div({'class_name': 'pt:mt-0 mx-auto flex flex-col items-center justify-center px-6 pt-8 md:h-screen'},
        link(
            html.div({'class_name': 'mb-8 flex items-center justify-center text-2xl font-semibold lg:mb-10'},
                html.img({'src': 'https://demo.themesberg.com/windster/images/logo.svg', 'class_name': 'mr-4 h-10', 'alt': 'React/Py Logo'}),
                html.span({'class_name': 'self-center whitespace-nowrap text-2xl font-bold'}, "React/Py")
            ),
            to='/'
        ),
        html.div({'class_name': 'w-full rounded-lg bg-white shadow sm:max-w-screen-sm md:mt-0 xl:p-0'},
            html.div({'class_name': 'space-y-8 p-6 sm:p-8 lg:p-16'},
                html.h2({'class_name': 'text-2xl font-bold text-gray-900 lg:text-3xl'}, title),
                form
            )
        )
    )
