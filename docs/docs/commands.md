⚠️ Notes
Use virtual environment (recommended)
Ensure Python is added to PATH


---

#  `commands.md` (Main professional section)

```md
#  Command Reference

---

## 🏗 startproject

Create a new Django project.

```bash
django-facile startproject <project_name> --env dev --db sqlite
```

Create a new Django app
```bash
django-facile startapp <app_name>
```
## switch environment
```bash
django-facile switch-env dev   # to development
django-facile switch-env prod  # to production
```

# Start django development server
```bash
django-facile run
```

# Makemigration & Migrate in one command
```bash
django-facile migrate
```

# Create superuser
```bash
django-facile superuser
```

# django shell for testing
```bash
django-facile shell
```

# Validate project configuration
```bash
django-facile check
# for production validation
django-facile check --deploy
```

# Collect static files for production.
```bash
django-facile collectstatic
```

# help
```bash
django-facile --help
```

# version
```bash
django-facile --version
```