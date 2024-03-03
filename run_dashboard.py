from app_main import AppMain
from utils.server_options.dashboard_options import DASHBOARD_OPTIONS
from utils.fast_server import run
from utils.find_port import find_available_port

# python run_dashboard.py

if __name__ == "__main__":
    port = find_available_port()
    run(AppMain, port=port, disable_server_logs=True, options=DASHBOARD_OPTIONS)
