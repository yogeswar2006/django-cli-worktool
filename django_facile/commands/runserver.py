import os
import subprocess
from dotenv import load_dotenv

def handle_runserver(args):
    load_dotenv()

    print("Starting server...")

    if not os.path.exists("manage.py"):
        print("Error: manage.py not found. Run inside Django project.")
        return
    env = os.getenv("ENV", "dev")

    if env == "prod":
        print("⚠ Running Django dev server in PRODUCTION mode is not recommended")
        print(" Use gunicorn or a production server instead\n")

    port = args.port if hasattr(args, "port") else "8000"

    try:
        subprocess.run(
            ["python", "manage.py", "runserver", f"127.0.0.1:{port}"]
        )
    except KeyboardInterrupt:
        print("\nServer stopped by user")

    