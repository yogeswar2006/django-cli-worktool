import subprocess

def handle_check(args):
    cmd = ["python", "manage.py", "check"]

    if args.deploy:
        cmd.append("--deploy")

    subprocess.run(cmd)