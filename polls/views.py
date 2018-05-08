from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Question

def index(request: HttpRequest) -> HttpResponse:
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    body = ', '.join(q.question_text for q in latest_questions)
    return HttpResponse(body)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at question %s" % question_id)

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at the results of question %s" % question_id)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s" % question_id)