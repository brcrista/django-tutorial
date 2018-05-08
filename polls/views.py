from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from .models import Question

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'latest_questions': Question.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'polls/index.html', context)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', { 'question': q })

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at the results of question %s" % question_id)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s" % question_id)