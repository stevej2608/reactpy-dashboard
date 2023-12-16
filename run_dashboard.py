from pages.app_main import AppMain
from fast_server import run

# python run_dashboard.py

if __name__ == "__main__":
    run(AppMain, disable_server_logs=True)
