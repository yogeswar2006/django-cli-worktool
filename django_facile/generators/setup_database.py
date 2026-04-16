import re
import os


def setup_database(name,db):
    settings_path = os.path.join(name,"settings","base.py")

    with open(settings_path, "r") as f:
        content = f.read()

    #  Remove existing DATABASES block
    content = re.sub(
        r"DATABASES\s*=\s*{.*?}\n}",
        "",
        content,
        flags=re.DOTALL
    )

    #  Add new DB config
    if db == "sqlite":
        new_db = """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
    elif db == "postgres":
        new_db = """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""

    # Append at end
    content += "\n" + new_db

    with open(settings_path, "w") as f:
        f.write(content)

    print(" Database configured:", db)