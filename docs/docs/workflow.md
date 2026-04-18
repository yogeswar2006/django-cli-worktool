
---

#  `workflow.md`
---



### Step 1: Create project
### Step 2: Create app
### Step 3: Run migrations
### Step 4: Test code in development mode
### Step 5: Switch to production mode
### Step 6: Configure Credentials in .env file
### step 7: Collect static files
### Step 8: Check deploy issues (misconfigurations)
---
##### NOTE:Dont try to run all these commmands at once(run one by one)
---
## **Development workkflow**
```bash
django-facile startproject myproject --env dev --db sqlite
cd myproject
django-facile startapp blog
django-facile migrate
django-facile run
```
---
## **Production workflow**
```bash

django-facile switch-env prod
django-facile migrate
django-facile collectstatic
django-facile check --deploy
```
