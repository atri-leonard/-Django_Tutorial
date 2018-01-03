from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.
# A real simple index view
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# Returns a page with question id
def detail(request, question_id):
    # Get question via question ID
    question = get_object_or_404(Question, pk=question_id)
    # Raise http 404 when there's no question
    return render(request, 'polls/detail.html', {'question': question})


# Returns a page with question result of corresponding id
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Returns a page with question that prompts vote options
def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)



