from pages.app_main import AppMain
from fast_server import run

# python dashboard.py

if __name__ == "__main__":
    run(AppMain, disable_server_logs=True)