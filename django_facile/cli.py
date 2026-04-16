import argparse
from django_facile.commands.startproject import handle_startproject
from django_facile.commands.createapp import handle_createapp
from django_facile.commands.addredis import handle_addredis

def main():
    parser = argparse.ArgumentParser(prog="django-facile")
    subparsers=parser.add_subparsers(dest="command")
    
    # for starting the project
    start=subparsers.add_parser("startproject")
    start.add_argument("name")
    start.add_argument("--env",default="dev")
    start.add_argument("--db",default="sqlite")
    
    # for creating the additional app
    create=subparsers.add_parser("createapp")
    create.add_argument("name")
    
    args=parser.parse_args()
    
    if args.command=="startproject":
        print(".......... creating project ..........")
        handle_startproject(args)
    elif args.command=="createapp":
        handle_createapp(args)
    elif args.command=="addredis":
        handle_addredis(args)