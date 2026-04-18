import argparse
from django_facile.commands.startproject import handle_startproject
from django_facile.commands.createapp import handle_createapp
from django_facile.commands.addredis import handle_addredis
from django_facile.commands.switchEnv import handle_switch_env
from django_facile.commands.runserver import handle_runserver
from django_facile.commands.migrate import handle_migrate
from django_facile.commands.superuser import handle_superuser
from django_facile.commands.shell import handle_shell
from django_facile.commands.check import handle_check
from django_facile.commands.static import handle_static

def main():
    parser = argparse.ArgumentParser(prog="django-facile",
                                    description="Django Facile - Simplify Django development",
                                    formatter_class=argparse.RawTextHelpFormatter)
    subparsers=parser.add_subparsers(dest="command",required=True)
    
    # for starting the project
    start=subparsers.add_parser("startproject",help="Start django project")
    start.add_argument("name",help="Django project name")
    start.add_argument("--env",default="dev",help="Project environment(dev or prod)")
    start.add_argument("--db",default="sqlite",help="Project database(sqlite or postgres)")
    
    # for creating the additional app
    create=subparsers.add_parser("startapp",help="Start app")
    create.add_argument("name",help="App name")
    
    
    parser.add_argument(
        "--version",
        action="version",
        version="django-facile 1.0.0"
    )
    
    switch=subparsers.add_parser("switch-env",help="Switch environment")
    switch.add_argument("name",help="environment name to be switched")
    
    run = subparsers.add_parser("run",help="start development server")
    run.add_argument("--port", default="8000",help="server port")
    
    migrate=subparsers.add_parser("migrate",help="Makemigrations & migrate")
    
    superuser= subparsers.add_parser('superuser',help="create superuser")
    
    shell = subparsers.add_parser("shell",help="shell")
    
    check= subparsers.add_parser("check",help="check issues in configuration")
    check.add_argument("--deploy",action="store_true",help="check issues in production mode")
    
    collectstatic=subparsers.add_parser("collectstatic",help="collectstatic files")
    
    args=parser.parse_args()
    
    if args.command=="startproject":
        print(".......... creating project ..........")
        handle_startproject(args)
    elif args.command=="startapp":
        handle_createapp(args)
    elif args.command=="run":
        handle_runserver(args)
    elif args.command=="switch-env":
        handle_switch_env(args)
    elif args.command=="migrate":
        handle_migrate()
    elif args.command=="superuser":
        handle_superuser()
    elif args.command=="shell":
        handle_shell()
    elif args.command=="check":
        handle_check(args)
    elif args.command=="collectstatic":
        handle_static()
    elif args.command=="addredis":
        handle_addredis(args)