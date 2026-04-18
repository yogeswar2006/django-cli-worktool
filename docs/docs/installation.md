
---

#  `installation.md`

---

### Create virtual env (Best Practice)
```bash
python -m venv venv
```
### activate venv
### for windows
```bash
venv/scripts/activate
```
### for linux 
```bash
source venv/bin/activate

```

##  Install via pip

```bash
pip install django-facile
```

### Verify the installation
```bash
django-facile --help
```
### Check version
```bash
django-facile --version
```


## Project structure (After creating project)
```bash
myproject/
├── manage.py
├── settings/
├── apps/
├── urls.py
├── asgi.py
├── wsgi.py
├── .env
├── .gitignore
```