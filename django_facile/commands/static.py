
import subprocess

def handle_static():
    cmd=["python","manage.py","collectstatic"]
    subprocess.run(cmd)