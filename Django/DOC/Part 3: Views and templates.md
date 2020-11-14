# Writing your first Django app, part 3    
* Django views serve the purpose of encapsulation. They encapsulate the logic liable for processing a user’s request and    
for returning the response back to the user.   
* Views in Django either return an HttpResponse or raise an exception such as Http404.  
* HttpResponse contains the objects that consist of the content that is to be rendered to the user.    
* Views can also be used to perform tasks such as read records from the database, displays the contain etc.   
* Each view is represented by a Python function (or method, in the case of class-based views).  
* Django will choose a view by examining the URL that’s requested.   
* To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.   
  
##### Writing more views   
* writing view`polls/views.py`   
```` 
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
````  
* Mapping view `polls/urls.py`   
``` 
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
##### Write views that actually do something  

* There way to write view but the url configuration is same i.e `polls/urls.py`    
```  
# polls/urls.py 
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name = 'index'),
 ]
``` 
1. view without template.   
``` 
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```       
