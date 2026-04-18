
import subprocess
import os

def handle_shell():
    if not os.path.exists("manage.py"):
        print("Error: manage.py not found.")
        return

    subprocess.run(["python", "manage.py", "shell"])
    