# 🚀 Django Facile

**Django Facile** is a powerful CLI tool that simplifies Django development by automating project setup, environment management, and common workflows.

---

## ✨ Features

* ⚡ One-command project setup
* 🔄 Dev ↔ Prod environment switching
* 🛠 Built-in commands for migrations, shell, server
* 🔐 Production-ready configuration helpers
* 📦 Simplified Django workflow

---

## 📦 Installation

```bash
pip install django-facile
```

---

## 🚀 Quick Start

```bash
django-facile startproject myproject --env dev --db sqlite
cd myproject
django-facile run
```

---

# 📚 Commands Overview

| Command       | Description                         |
| ------------- | ----------------------------------- |
| startproject  | Create a Django project             |
| startapp      | Create a Django app                 |
| switch-env    | Switch environment (dev/prod)       |
| run           | Start development server            |
| migrate       | Run makemigrations + migrate        |
| superuser     | Create admin user                   |
| shell         | Open Django shell                   |
| check         | Validate project configuration      |
| collectstatic | Prepare static files for production |
| --help        | Show CLI help                       |
| --version     | Show CLI version                    |

---

# 🧠 Environment Modes

## 🧪 Development Mode (dev)

* Uses **SQLite**
* DEBUG = True
* Auto static serving
* Faster development

## 🚀 Production Mode (prod)

* Uses **PostgreSQL**
* DEBUG = False
* Requires `collectstatic`
* Security settings enabled

---

# ⚙️ Commands (Detailed)

---

## 🏗 Create Project

```bash
django-facile startproject <project_name> --env dev --db sqlite
```

### Example:

```bash
django-facile startproject myproject --env dev --db sqlite
```

---

## 📦 Create App

```bash
django-facile startapp <app_name>
```

### Example:

```bash
django-facile startapp blog
```

---

## 🔄 Switch Environment

### Switch to Development:

```bash
django-facile switch-env dev
```

### Switch to Production:

```bash
django-facile switch-env prod
```

---

## ▶️ Run Server

```bash
django-facile run
```

### Custom port:

```bash
django-facile run --port 8001
```

---

## 🗄 Database Migrations

```bash
django-facile migrate
```

👉 Internally runs:

* `makemigrations`
* `migrate`

---

## 👤 Create Superuser

```bash
django-facile superuser
```

---

## 🐚 Django Shell

```bash
django-facile shell
```

---

## 🔍 Check Configuration

### Normal check:

```bash
django-facile check
```

### Production check:

```bash
django-facile check --deploy
```

---

## 📦 Collect Static Files (Production Only)

```bash
django-facile collectstatic
```

⚠️ Use only in **production mode**

---

## 📖 Help

```bash
django-facile --help
```

---

## 🔢 Version

```bash
django-facile --version
```

---

# 🔄 Typical Workflow

## 🧪 Development Workflow

```bash
django-facile startproject myproject --env dev --db sqlite
cd myproject
django-facile startapp blog
django-facile run
```

---

## 🚀 Production Workflow

```bash
django-facile switch-env prod
django-facile migrate
django-facile collectstatic
django-facile check --deploy
```

---

# ⚠️ Important Notes

* `collectstatic` is **only required in production**
* `check --deploy` should be run before deployment
* `.env` controls active environment
* Dev and Prod configs are separated internally

---

# 🧠 Why Django Facile?

Django setup and environment management can be repetitive and error-prone.
Django Facile simplifies the workflow into a clean, developer-friendly CLI.

---

# 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

# 📄 License

MIT License
