# Writing your first Django app, part 1   

Throughout this tutorial, we’ll walk you through the creation of a basic poll application.   
It’ll consist of two parts:   
    
* A public site that lets people view polls and vote in them.   
* An admin site that lets you add, change, and delete polls.      

**install and version of django**   
* `$  pip install django`   
* `$  python -m django --version`       
   
**Note**  Django 3.1, which supports Python 3.6 and later.   

## create django project   
    
*` $ django-admin startproject mywebsite`   
* structure of project   
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
**manage.py** : A command-line utility that lets you interact with this Django project in various ways.      
**__init__.py** : An empty file that tells Python that this directory should be considered a Python package.     
**settings.py**A Django settings file contains all the configuration of your Django installation.      
``` Example     
ALLOWED_HOSTS = ['www.example.com']
DEBUG = False
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
```
**urls.py**: The URL declarations for this Django project.      
**asgi.py**: An entry-point for ASGI-compatible web servers to serve your project.      
**wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project.     

## The development server   

* `$ python manage.py runserver`    
* **http://127.0.0.1:8000/** run on web browser.   
* Automatic reloading of runserver  
The development server automatically reloads Python code for each request as needed. You don’t need to restart the server   
for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart   
the server in these cases.    
* Changing the port    
By default, the runserver command starts the development server on the internal IP at port 8000.
If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server  
on **port 8080** `$ python manage.py runserver 8080`    

## Creating the Polls app   
      
* Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on    
writing code rather than creating directories.         
  
*  Projects vs. apps   

Projects | apps  
--- |---
 A project is a collection of configuration and multiple apps for a particular website|An app is a Web application that does something.   
 .| e.g., a Weblog system, a database
 .|An app can be in multiple projects.
* To create your app, make sure you’re in the same directory as manage.py and type this command.   
`$ python manage.py startapp polls`      
* polls, which is laid out like this.  
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
  
## Write your first view 
* polls/views.py   
``` 
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```   
* To call the view, we need to map it to a URL and for this we need a URLconf.   
* polls/urls.py     

```   
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
* To point the root URLconf at the `polls.urls.py` module. By `mywebsite/urls.py` using include() in the urlpatterns list.     
**include()** function allows referencing other URLconfs. Whenever Django encounters include(), it chops/cut off whatever         
part of the URL matched up to that point and sends the remaining string to the included URL configuration for further processing.    

**Note** http://localhost:8000/polls/ it return “Hello, world. You’re at the polls index.” and http://localhost:8000/       
not return “Hello, world. You’re at the polls index.”     

### question   
1. polls/views.py how to add multiple views.   
2. can we create multiple views.py ?  
3. polls.urls.py what is the use of first argument of path('').   
4. how to break down the url in `mywebsite/urls.py`. eg. polls/homepage. or polls/contact. etc. 

#### my problem solve question 3 and 4.    
1. `mywebsite/urls.py` we use include `path('polls/', include('polls.urls'))` . polls is the base url means start url.   
2.  polls/urls.py have url configuration. in path first argument is use after base url.  
example  
``` 
urlpatterns = [
    path('', views.index, name = 'index'),
    path('homepage/', views.homepage, name= 'homepage' )
]
``` 
`http://127.0.0.1:8020/polls/homepage/`  
view.homepage is display **This is home page**   

 
   