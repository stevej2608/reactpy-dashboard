import logging

logging.basicConfig(
    format='%(levelname)s %(asctime)s %(module)12s/%(lineno)-5d %(message)s',
    datefmt='%H:%M:%S'
)

log: logging.Logger = logging.getLogger()


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
    "uvicorn.access",
    "starlette",
]


def disable_noisy_logs():
    # Turn off noisy logging

    for log_id in LOGS:
        _log = logging.getLogger(log_id)
        _log.setLevel(logging.ERROR)
