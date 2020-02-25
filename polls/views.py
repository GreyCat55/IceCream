from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pdate')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }    
    return render(request, 'polls/index.html', context)

# Create your views here.

def detail(request, questionID):
    return HttpResponse("I have one simple question for you: %s" % questionID)

def results(request, questionID):
    response = "For those who answered %s"
    return HttpResponse(response % questionID)

def vote(request, questionID):
    return HttpResponse("So tell me: %s" % questionID)