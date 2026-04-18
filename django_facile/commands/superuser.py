import subprocess
import os

def handle_superuser():
    if not os.path.exists("manage.py"):
        print("Error: manage.py not found. Run inside Django project.")
        return

    print("Creating superuser...")

    try:
        subprocess.run(
            ["python", "manage.py", "createsuperuser"],
            check=True
        )
        

    except subprocess.CalledProcessError:
        print("Failed to create superuser")

    except KeyboardInterrupt:
        print("\nCancelled by user")