from typing import Any

import uvicorn

from app_main import AppMain
from manager import cli
from utils.server_options.dashboard_options import DASHBOARD_OPTIONS
from utils.fast_server import run
from utils.logger import log, logging


@cli.command()
def runserver(**kwargs: Any):
    """Run the uvicorn server"""

    log.setLevel(logging.INFO)

    if "log_level" not in kwargs:
        kwargs["log_level"] = logging.WARNING

    run(AppMain, options=DASHBOARD_OPTIONS, **kwargs)



# Hack: clone all the uvicorn cli options and add them to
# our runserver stub. This allows the stub to act as a fully
# featured CLI command with all the uvicorn options listed
# in the cli/click help system

cli.commands["runserver"].params = uvicorn.main.params[1:]
