from django_facile.generators.create_env import create_env
from django_facile.generators.create_project import create_project
from django_facile.generators.setup_settings import setup_settings
from django_facile.generators.setup_database import setup_database


def handle_startproject(args):
    
    create_project(args.name)   # this will create default django project
    setup_settings(args.name,args.env)  # this will configure best way to handle settings(both dev and prod) 
    setup_database(args.name,args.db)  # this will configure both sqlite and postgres config
    create_env(args.name,args.env)  # this will configure .env file (default)