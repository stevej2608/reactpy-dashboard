import inspect
from types import FunctionType
import os
import sys
from pathlib import Path
from typing import Any, Callable

from exceptiongroup import ExceptionGroup

import uvicorn
from fastapi import FastAPI, Request
from reactpy import html
from reactpy.backend.fastapi import Options as FastApiOptions
from reactpy.backend.fastapi import configure
from reactpy.core.component import Component
from starlette.websockets import WebSocketDisconnect

from utils.logger import log, logging, disable_noisy_logs
from utils.server_options.assets import assets_api
from utils.server_options.default_options import DEFAULT_OPTIONS, ServerOptions
from utils.var_name import var_name

# pyright: reportDeprecated=false
# pyright: reportUnusedFunction=false

app = FastAPI(description="ReactPy", version="0.1.0")



def extract_wrapped(decorated: Callable[..., Component]) -> FunctionType:
    """Return the FunctionType object for the functions wrapped by @component"""

    # https://stackoverflow.com/a/43506509/489239

    closure = (c.cell_contents for c in decorated.__closure__)  # type: ignore
    func = next((c for c in closure if isinstance(c, FunctionType)), None)

    if func is None:
        raise AssertionError('Unable to extract function reference from wrapper')

    return func

def run(
    app_main: Callable[[], Component],
    options: ServerOptions = DEFAULT_OPTIONS,
    host: str = "127.0.0.1",
    port: int = 8000,
    disable_server_logs: bool = True,
    **kwargs: Any,
) -> None:
    """Called once to run reactpy application on the fastapi server

    Args:
        app_main (Callable[[], Component]): Function that returns a reactpy Component
        options (Options, optional): Server options. Defaults to DASHBOARD_OPTIONS.

    Usage:
    ```
            @component
            def AppMain():
                return html.h2('Hello from reactPy!')
                )

            run(AppMain, options=PICO_OPTIONS)

    ```
    """

    def _app_path(app: FastAPI) -> str:
        app_str = var_name(app, globals())
        return f"{__name__}:{app_str}"

    # Mount any fastapi end points here

    if options.asset_folder == "assets":
        func = extract_wrapped(app_main)
        asset_folder = Path(inspect.getfile(func)).parent.relative_to(os.getcwd())
        options.asset_folder = str(asset_folder)

    app.mount("/" + options.asset_root, assets_api(options))

    opt = FastApiOptions(head=html.head(*options.head))

    configure(app, app_main, options=opt)

    app_path = _app_path(app)


    @app.exception_handler(ExceptionGroup)
    def websocket_disconnect_handler(request: Request, exc: ExceptionGroup):
        if len(exc.exceptions) == 1 and isinstance(exc.exceptions[0], WebSocketDisconnect):
            websocket_disconnect = exc.exceptions[0]

            code = websocket_disconnect.code

            # Code 1001 indicates that an endpoint is "going away", such as a server going
            # down or a browser having navigated away from a page. Ignore these.

            # 1002 indicates that an endpoint is terminating
            # the connection due to a protocol error.

            if code != 1001:
                log.info("WebSocket %s disconnected with code %s", request.url, code)

        else:
            # If it's not a WebSocketDisconnect, re-raise the exception
            raise exc

    @app.on_event('startup')
    async def fastapi_startup():
        if disable_server_logs:
            disable_noisy_logs()
        log.info("Uvicorn running on  http://%s:%s (Press CTRL+C to quit)", host, port)


    try:
        log.setLevel(logging.INFO)
        uvicorn.run(app_path, host=host, port=port, **kwargs) # type: ignore
    except Exception as ex:
        log.info("Uvicorn server %s\n", ex)
    finally:
        print("\b\b")
        log.info("Uvicorn server has shut down\n")
        sys.exit(0)
