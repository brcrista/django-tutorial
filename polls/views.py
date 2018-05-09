from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'polls/index.html', {
        'latest_questions': Question.objects.order_by('-pub_date')[:5]
    })

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { 'question': question })

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at the results of question %s" % question_id)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))