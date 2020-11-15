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

* Three way to write view but the url configuration is same i.e `polls/urls.py`   
* This is common for there way to write view.      
```  
# polls/urls.py 
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name = 'index'),
 ]
``` 
**1** view without template.   
``` 
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```       
**2** view using template but use `from django.template import loader`  
```   
from django.template import loader  

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```   
**3** view using template but use `from django.shortcuts import render`    
```   
from django.shortcuts import render  

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

``` 

####  raise Http404   
* Two way to handel raise Http404.   
**1** using try except  
```  
from django.http import Http404
def details(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("question is not exist")
    return render(request, 'polls/details.html', {'question' :question})
``` 
**2** without using try except.  
```  
from django.shortcuts import get_object_or_404, render

def details(request, question_id):

    question =  get_object_or_404(Question, pk =question_id)
    return render(request, 'polls/details.html', {'question' :question})
```   
##### Use the template system   
* The template system uses dot-lookup syntax to access variable attributes. . In the example of {{ question.question_text }}.  
* first Django does a dictionary lookup on the object question. Failing that, it tries an attribute lookup – which works, in this case.  
* . If attribute lookup had failed, it would’ve tried a list-index lookup.

##### Removing hardcoded URLs in templates   
* first we use   
`<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>`  
* change and use.  
`<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>`   
##### Namespacing URL names 
* app_name to set the application namespace.    
**polls/urls.py** 
``` 
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```  
* first use this old method. `polls/templates/polls/index.html `   
``` 
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li> 
```    
* using namespace `polls/templates/polls/index.html `     
`<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>` 