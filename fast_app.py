from fastapi import FastAPI
from reactpy.backend.fastapi import configure

from app_main import MainApp

app = FastAPI(description="ReactPy", version="0.1.0")


def init_fastapp():
    configure(app, MainApp)
