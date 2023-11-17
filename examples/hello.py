from reactpy import component, html, run

GREETING = 'Hello, World!'

@component
def AppMain():
    element = html.h2(GREETING)
    return html.div(
        element
    )

# python examples/hello.py

# Internally app is run by Uvicorn/starlette


if __name__ == "__main__":
    run(AppMain, host="0.0.0.0", port=8000)
