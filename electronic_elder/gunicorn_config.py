from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BASE_DIR_PARENT = Path(__file__).resolve().parent.parent

command = f"{BASE_DIR}/env/bin/gunicorn"
pythonpath = f"{BASE_DIR}"
bind = "127.0.0.1:8000"
workers = 5
user = "tran1l"
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = "DJANGO_SETTINGS_MODULE=electronic_elder.settings"
