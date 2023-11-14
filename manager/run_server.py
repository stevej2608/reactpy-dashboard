import uvicorn
from manager import cli
from utils.logger import log, logging

from fast_server import app, run
from pages.app_main import AppMain

LOGS = [
    "asgi-logger",
    "concurrent.futures",
    "concurrent",
    "asyncio",
    "uvicorn.error",
    "uvicorn",
    "watchfiles.watcher",
    "watchfiles",
    "watchfiles.main",
    "fastapi",
    "reactpy.backend",
    "reactpy",
    "reactpy._option",
    "reactpy.core.hooks",
    "reactpy.core",
    "urllib3.util.retry",
    "urllib3.util",
    "urllib3",
    "urllib3.connection",
    "urllib3.response",
    "urllib3.connectionpool",
    "urllib3.poolmanager",
    "charset_normalizer",
    "requests",
    "reactpy.web.utils",
    "reactpy.web",
    "reactpy.web.module",
    "reactpy.backend.utils",
    "reactpy.core.layout",
    "reactpy.core.serve",
    "reactpy.backend.starlette",
    "starlette",
]


def disable_noisy_logs():
    # Turn off noisy logging

    for log_id in LOGS:
        _log = logging.getLogger(log_id)
        _log.setLevel(logging.ERROR)


@cli.command()
def runserver(**kwargs):
    """Run the uvicorn server"""

    log.setLevel(logging.INFO)

    if "log_level" not in kwargs:
        kwargs["log_level"] = logging.WARNING

    @app.on_event('startup')
    async def fastapi_startup():
        disable_noisy_logs()
        log.info(f"Uvicorn running on  http://%s:%s/ (Press CTRL+C to quit)", kwargs['host'], kwargs['port'])

    run(AppMain, **kwargs)



# Hack: clone all the uvicorn cli options and add them to
# our runserver stub. This allows the stub to act as a fully
# featured CLI command with all the uvicorn options listed
# in the cli/click help system

cli.commands["runserver"].params = uvicorn.main.params[1:]
