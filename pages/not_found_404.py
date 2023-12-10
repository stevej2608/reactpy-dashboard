from reactpy import component, html, event



@component
def NoFoundPage(*args, **kwargs):
    return html.section({'class_name': 'flex items-center h-full p-16 dark:bg-gray-900 dark:text-gray-100'},
        html.div({'class_name': 'container flex flex-col items-center justify-center px-5 mx-auto my-8'},
            html.div({'class_name' :'max-w-md text-center'},
                html.h2({'class_name': 'mb-8 font-extrabold text-9xl dark:text-gray-600'}, html.span({'class_name': 'sr-only'}, "Error","404")),
                html.p({'class_name': 'text-2xl font-semibold md:text-3xl'}, "Sorry, we couldn't find this page."),
                html.p({'class_name': 'mt-4 mb-8 dark:text-gray-400'}, "But dont worry, you can find plenty of other things on our homepage."),
                html.a({'class_name': 'px-8 py-3 font-semibold rounded dark:bg-violet-400 dark:text-gray-900', 'rel': 'noopener noreferrer', 'href': '/'}, "Back to homepage")
            )
        )
    )
