from reactpy import component, html, run


@component
def AppMain():

    element = html.h2('Hello World')


    return html.div(
        element
    )


if __name__ == "__main__":
    run(AppMain, port=3000)
