import os
import subprocess

def add_to_installed_apps(settings_path, name):
    with open(settings_path, "r") as f:
        lines = f.readlines()
        
    app_entry = f'    "apps.{name}",\n'

    inside = False
    for i, line in enumerate(lines):
        if "INSTALLED_APPS" in line:
            inside = True
        elif inside and "]" in line:
            # insert before closing bracket
            lines.insert(i, app_entry)
            break

    with open(settings_path, "w") as f:
        f.writelines(lines)
    print("Created App added to Installed apps")

def fix_app_config(app_path, name):
    apps_file = os.path.join(app_path, "apps.py")

    with open(apps_file, "r") as f:
        content = f.read()

    content = content.replace(
        f'name = "{name}"',
        f'name = "apps.{name}"'
    )

    with open(apps_file, "w") as f:
        f.write(content)
    print("Updated apps.py path")





def create_app(args):
    name = args.name
    app_path = os.path.join("apps", name)

    os.makedirs(app_path, exist_ok=True)

    result = subprocess.run(
        ['python', 'manage.py', 'startapp', name, app_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Error:", result.stderr)
        return

    print("App created successfully")

    BASE_DIR = os.getcwd()
    settings_path = os.path.join(BASE_DIR, "settings", "base.py")

    add_to_installed_apps(settings_path, name)
    fix_app_config(app_path,name)
    
    