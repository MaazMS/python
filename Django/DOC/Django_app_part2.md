# Writing your first Django app, part 2    

* We’ll setup the database, create your first model, and get a quick introduction to Django’s automatically-generated admin site.   
* By default, Django uses SQLite database. if you want to change database `mywebsite/settings.py`   
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```  
* install apps which are use in django project. example install polls `'polls.apps.PollsConfig',` in `mywebsite/settings.py`  
* `python manage.py migrate` use this command for install apps.  

## Creating models  

Q1. What are ‘Models’?  
Models are a single and definitive(general use) source for information about your data. It consists of all the essential    
fields and behaviors of the data you have stored. Often, each model will map to a single specific database table.   
In Django, models serve as the abstraction layer that is used for structuring and manipulating your data. Django models   
are a subclass of the django.db.models.Model class and the attributes in the models represent database fields.     

* poll app, we’ll create two models: Question and Choice.    

Question | Choice 
|--- | --- | 
A Question has a question and a publication date.|  
example question_text and pub_date. | Choice has two fields `text` of the choice and a `vote tally`   
.| Each Choice is associated with a Question.     

* polls/models.py   
``` 
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
****

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```  
1. CharField for character fields.  
2. DateTimeField for datetimes.  
3. Default value of votes to 0.   
4. using ForeignKey each Choice is related to a single Question.   

## Activating models   

* Create a database schema.  
* Create a Python database-access API for accessing Question and Choice objects.   
**But first we need to tell our project that the polls app is installed.**  
`mysite/settings.py`   
```` 
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
````  
* run this command `$ python manage.py makemigrations polls`     
**Note** makemigrations tells Django you have created/ changed your models.  
read the migration  file polls/migrations/0001_initial.py. or `$ python manage.py sqlmigrate polls 0001` it return SQL.   

* run migrate again to create those model tables in your database. `$ python manage.py migrate`. migrate command looks at   
the INSTALLED_APPS settings and creates database tables accordingly     

**Note** If you’re interested, you can also run python manage.py check; this checks for any problems in your project    
without making migrations or touching the database.     

``` 
remember the three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
```  
## Playing with the API    

* These are all command work in python shell. `$ python manage.py shell`   

##### create question
* create question import Question and timezone. 
* create Question model in polls/models.py.   
* add question eg. **q = Question(question_text="What's new?", pub_date=timezone.now())**  
* save question explicitly **q.save()**   
```  
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.
>>> from django.utils import timezone 
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
# Save the object into the database. You have to call save() explicitly.
```  
##### Access model field values via Python attributes.
* It show last value for the attribute.    
``` 
>>> q.pub_date
>>> q.question_text
``` 
##### Change values of attributes, then calling save().  
``` 
>>> q.question_text = "What's up?"
>>> q.save()
``` 

###### displays all the questions in the database.  
`>>> Question.objects.all()`  

###  representation of this object Question and Choice   

use inside of model Question and model Choice.  
```
def __str__(self):
        return self.question_text
def __str__(self):
        return self.choice_text
``` 
##### Question search by id  and primary key. 
* shortcut for primary-key is `pk`    
`>>> Question.objects.filter(id=1)`
`>>> Question.objects.get(pk=1)`   
* if question is not available then it through error **polls.models.Question.DoesNotExist: Question matching query does not exist.**
  
#####  Create three choices.  
* `choice_set` is **RelatedManager** which can create query sets.      
`c = q.choice_set.create(choice_text='Just hacking again', votes=0)`   

* count choice ` >>> >>> q.choice_set.count()`
* Let's delete one of the choices. Use delete() for that.

``` 
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
(1, {'polls.Choice': 1})
```
##### Introducing the Django Admin 
* Philosophy   

Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require  
much creativity. For that reason, Django entirely automates creation of admin interfaces for models.   

Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public”   
site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the    
public site. Django solves the problem of creating a unified interface for site administrators to edit content.   
The admin isn’t intended to be used by site visitors. It’s for site managers.      

##### Creating an admin user  

* `$ python manage.py createsuperuser`   
1. Enter your desired username and press enter.  
`Username: admin`  
2. You will then be prompted for your desired email address:   
`Email address: admin@example.com`     
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first   
``` 
Password: **********
Password (again): *********
Superuser created successfully.
``` 
##### Start the development server 
   
`$ python manage.py runserver`   
`http://127.0.0.1:8000/admin/.`    

##### Make the poll app modifiable in the admin  
But where’s our poll app? It’s not displayed on the admin index page.  
* register poll app from `polls/admin.py`   
```` 
from django.contrib import admin
from .models import Question
admin.site.register(Question)

````
 
 * Each DateTimeField gets free JavaScript shortcuts. Dates get a “Today” shortcut and calendar popup, and times get a   
 “Now” shortcut and a convenient popup that lists commonly entered times.  
  