import subprocess
import os

def handle_migrate():
    if not os.path.exists("manage.py"):
        print("Error: manage.py not found.")
        return

    print("Applying migrations...")

    try:
        subprocess.run(["python", "manage.py", "makemigrations"], check=True)
        subprocess.run(["python", "manage.py", "migrate"], check=True)
        print("Migrations created")
        print("Migrations applied to database successfully")

    except subprocess.CalledProcessError:
        print("Migration failed")

    except KeyboardInterrupt:
        print("\nMigration cancelled")