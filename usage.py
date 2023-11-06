import sys
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
import uvicorn

from app_main import MainApp

app = FastAPI()
configure(app, MainApp)

if __name__ == "__main__":
    uvicorn.run("usage:app")
