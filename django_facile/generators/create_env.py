import os
import secrets

def create_env(name, env):
    debug = "True" if env == 'dev' else "False"

    settings_path = os.path.join(name, "settings", "base.py")

    # Generate secure secret key
    secret_key = secrets.token_urlsafe(50)

    # Read settings file
    with open(settings_path, 'r') as f:
        content = f.read()

    # Add dotenv + env usage at top
    env_setup = """
import os
from dotenv import load_dotenv

load_dotenv()
"""

    # Replace SECRET_KEY
    new_lines = []

    for line in content.splitlines():
      if line.strip().startswith("SECRET_KEY"):
        new_lines.append('SECRET_KEY = os.getenv("SECRET_KEY")')
      elif line.strip().startswith("DEBUG"):
           new_lines.append('DEBUG = os.getenv("DEBUG")')
      else:
        new_lines.append(line)

    content = "\n".join(new_lines)

    # Write updated content
    with open(settings_path, 'w') as f:
        f.write(env_setup + content)

    # Create .env file
    with open(os.path.join(name, ".env"), 'w') as f:
        f.write(
            f"ENV={env}\n"
            f"DEBUG={debug}\n"
            f"SECRET_KEY={secret_key}\n"
        )

    print(" Configured .env file")