from django.http import HttpResponse
from  .models import Question
from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def homepage(request):
    return HttpResponse("This is home page")

def details(request, question_id):

    question =  get_object_or_404(Question, pk =question_id)
    return render(request, 'polls/details.html', {'question' :question})

def results(request, question_id):
    response = "you are looking at the result of question %s"
    return  HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are voting on question %s" % question_id)
