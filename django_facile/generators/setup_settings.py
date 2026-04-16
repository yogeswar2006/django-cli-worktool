import os
import shutil

# this function will update the settings file path in manage.py,wsgi.py,asgi.py
def update_settings_path(name,env):
    files =[
        f"{name}/manage.py",
        f"{name}/wsgi.py",
        f"{name}/asgi.py",
    ]
    
    for file in files:
        with open(file,'r') as f:
           lines = f.readlines()
        with open(file,'w') as f:
            for line in lines:
                if "DJANGO_SETTINGS_MODULE" in line:
                        indent = line[:len(line) - len(line.lstrip())]

                        f.write(
                            f"{indent}from dotenv import load_dotenv\n"
                            f"{indent}load_dotenv()\n"
                            f"{indent}env = os.getenv('ENV', 'dev')\n"
                            f"{indent}os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.{{env}}')\n"
                        )
                else:
                    f.write(line)

def setup_settings(name,env):
    base_path = f"{name}"

    old_settings = f"{base_path}/settings.py"
    new_settings_dir = f"{base_path}/settings"

    os.makedirs(new_settings_dir, exist_ok=True)

    # Move old settings to base.py
    shutil.move(old_settings, f"{new_settings_dir}/base.py")

    # Create dev.py
    with open(f"{new_settings_dir}/dev.py", "w") as f:
        f.write("from .base import *\nDEBUG=True\n")

    # Create prod.py
    with open(f"{new_settings_dir}/prod.py", "w") as f:
        f.write("from .base import *\nDEBUG=False\n")

    # init file
    open(f"{new_settings_dir}/__init__.py", "w").close()
    
    # need to modify manage.py & wsgi settings path
    update_settings_path(name,env)
    
    print(" Settings configured and updated manage.py & etc...")