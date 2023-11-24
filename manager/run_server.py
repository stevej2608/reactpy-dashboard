import uvicorn
from manager import cli
from utils.logger import log, logging

from fast_server import app, run
from pages.app_main import AppMain


@cli.command()
def runserver(**kwargs):
    """Run the uvicorn server"""

    log.setLevel(logging.INFO)

    if "log_level" not in kwargs:
        kwargs["log_level"] = logging.WARNING

    @app.on_event('startup')
    async def fastapi_startup():
        log.info(f"Uvicorn running on  http://%s:%s/ (Press CTRL+C to quit)", kwargs['host'], kwargs['port'])

    run(AppMain, **kwargs)



# Hack: clone all the uvicorn cli options and add them to
# our runserver stub. This allows the stub to act as a fully
# featured CLI command with all the uvicorn options listed
# in the cli/click help system

cli.commands["runserver"].params = uvicorn.main.params[1:]
