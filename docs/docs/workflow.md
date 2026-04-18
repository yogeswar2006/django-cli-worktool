
---

#  `workflow.md`

```md
#  Workflow Guide

---

##  Development Workflow

### Step 1: Create project
# NOTE:Dont try to run all these commmands at once(run one by one)
```bash
# Development workflow
django-facile startproject myproject --env dev --db sqlite
cd myproject
django-facile startapp blog
django-facile migrate
django-facile run

# Production workflow
django-facile switch-env prod
django-facile migrate
django-facile collectstatic
django-facile check --deploy
