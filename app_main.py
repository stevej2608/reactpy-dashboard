from reactpy import component, html, run

@component
def AppMain():
    element = html.h2('Hello World')
    return html.div(
        element
    )

# python app_main.py
#
# Internally app is run by Uvicorn/starlette
#

if __name__ == "__main__":
    run(AppMain, host="0.0.0.0", port=8000)