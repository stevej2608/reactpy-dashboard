import logging

logging.basicConfig(
    format='%(levelname)s %(asctime)s %(module)12s/%(lineno)-5d %(message)s',
    datefmt='%H:%M:%S'
)

log: logging.Logger = logging.getLogger()
