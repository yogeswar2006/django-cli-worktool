import os
import shutil

def create_project(name):
    # create project normally
    
    os.system(f"django-admin startproject {name}")
  
    
    # find inner app path
    inner=os.path.join(name,name)
    
    # move every inner file/folder to outer
    for item in os.listdir(inner):
        shutil.move(os.path.join(inner,item),os.path.join(name,item))
    
    # remove inner app(unneccessary)
    os.rmdir(inner)
    
    print(" Django project created:", name)
    