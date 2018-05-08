from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Question

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'latest_questions': Question.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'polls/index.html', context)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at question %s" % question_id)

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at the results of question %s" % question_id)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s" % question_id)