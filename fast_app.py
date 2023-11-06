import uvicorn
from fastapi import FastAPI
from reactpy.backend.fastapi import configure

from app_main import MainApp

app = FastAPI(description="ReactPy", version="0.1.0")

def init_fastapp(**kwargs) -> str:
    """Called once, just before server is started"""

    def package_prefix():
        return __package__ + '.' if __package__ else ''

    configure(app, MainApp)

    # Mount any fastapi end points here, eg:
    #   app.mount('/client', client_api)

    app_path = f"{package_prefix()}{__name__}:app"
    uvicorn.run(app_path, **kwargs)
