#### installation of django  
1. pip install django   

#### runserver   
1. create the project. `django-admin startoroject mywebsite` **mywebsite** is project name.     
2. structure of project   
``` 
mywebsite/
    manage.py
    mywebsite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
``` 
3. go to **mywebsite** `cd mywebsite/` and run the command `python manage.py runserver`  
4. open the chrome run url ` http://127.0.0.1:8000/`   
**manage.py** : A command-line utility that lets you interact with this Django project in various ways.    
**__init__.py** : An empty file that tells Python that this directory should be considered a Python package.   
**settings.py**A Django settings file contains all the configuration of your Django installation.   
``` Example    
ALLOWED_HOSTS = ['www.example.com']
DEBUG = False
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
```
**urls.py**: The URL declarations for this Django projec.   
**asgi.py**: An entry-point for ASGI-compatible web servers to serve your project.   
**wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project

#### Creating the Polls app   
* Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on  
 writing code rather than creating directories.  
* To create your app, make sure you’re in the same directory as manage.py.  
* command for polls `python manage.py startapp polls`   
* directory polls, which is laid out like this:   
``` 
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```   
*  Projects vs. apps   

Projects | apps  
--- |---
 A project is a collection of configuration and multiple apps for a particular website|An app is a Web application that does something.   
 .| e.g., a Weblog system, a database
 .|An app can be in multiple projects.

#### Write your first view   
1. polls/views.py write python code.     
2. URL configuration.
3. 