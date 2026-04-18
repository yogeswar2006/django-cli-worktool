
---

#  `installation.md`

```md
#  Installation

---

## Create virtual env (Best Practice)
```bash
python -m venv venv

## activate venv
# for windows
venv/scripts/activate

# for linux 
source venv/bin/activate
```

##  Install via pip

```bash
pip install django-facile

## Verify the installation
django-facile --help
## Check version
django-facile --version

```
## Project structure (After creating project)
myproject/
├── manage.py
├── settings/
├── apps/
├── urls.py
├── asgi.py
├── wsgi.py
├── .env
├── .gitignore