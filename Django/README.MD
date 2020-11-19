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
1. polls/views.py write the view.   
2. polls/urls.py URL configuration.(To call the view, we need to map it to a URL).   
3. point the root URL configuration at the polls.urls module. In mywebsite/urls.py.       
   
**include()** function allows referencing other URLconfs. Whenever Django encounters include(), it chops/cut off whatever     
part of the URL matched up to that point and sends the remaining string to the included URL configuration for further processing.    
   

**Note** http://localhost:8000/polls/ it return “Hello, world. You’re at the polls index.” and http://localhost:8000/     
not return “Hello, world. You’re at the polls index.”   

### admin interface     

* Creating models   
 models – essentially, your database layout, with additional metadata.   
 
* Question and choice 
 
Question | Choice 
|--- | --- | 
A Question has a question and a publication date.|  
example question_text and pub_date. | Choice has two fields `text` of the choice and a `vote tally`   
.| Question is reference in choice.   

### create questions and choice   
1. polls/models.py is add class question and choice.  
2. mywebsite/settings.py `INSTALLED_APPS` variable add ` 'polls.apps.PollsConfig',`  
3. run that command `python manage.py makemigrations polls` create Question and Choice.   
**makemigrations** you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones)    
and that you’d like the changes to be stored as a migration.  

very model have primary key.  
difference between get and filter.   
filter return single and multiple value.   
get return single and multiple value give error.  

#### Playing with the API  

* Create a new Question.  