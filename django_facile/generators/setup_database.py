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
    content = re.sub(
    r"ALLOWED_HOSTS\s*=\s*\[.*?\]\n",
    "",
    content,
    flags=re.DOTALL
    )

    # Remove STATIC settings (STATIC_URL, STATIC_ROOT, etc.)
    content = re.sub(
        r"STATIC_[A-Z_]*\s*=\s*.*\n",
        "",
        content
    )

    #  Add new DB config
    
    dev_db = """
        
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ["*"]

STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}
"""
    dev_path=os.path.join(name,"settings","dev.py")
    with open(dev_path,'a') as f:
            f.write(dev_db)
    
    prod_db = """
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DATABASE_NAME"),  # add your credentials in .env file 
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
    }
}
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]

STATIC_URL = "/static/"   # need to run python manage.py collectstatci
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

SECURE_SSL_REDIRECT = True   # only if using HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://yourdomain.com"
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}

CORS_ALLOWED_ORIGINS = [
    "https://frontend.com"
]
""" 
    prod_path=os.path.join(name,"settings","prod.py")
    with open(prod_path,'a') as f:
            f.write(prod_db)

    
    with open(settings_path, "w") as f:
        f.write(content)
        

    print(" Database configured:", db)