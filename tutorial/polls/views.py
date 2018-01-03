from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # Return most recent five questions
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# # Create your views here.
# # A real simple index view
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# # Returns a page with question id
# def detail(request, question_id):
#     # Get question via question ID
#     question = get_object_or_404(Question, pk=question_id)
#     # Raise http 404 when there's no question
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# # Returns a page with question result of corresponding id
# def results(request, question_id):
#     # Get question via question ID
#     question = get_object_or_404(Question, pk=question_id)
#     # Raise http 404 when there's no question
#     return render(request, 'polls/results.html', {'question': question})

# Returns a page with question that prompts vote options
def vote(request, question_id):
    # Get question lest
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Get choice that is selected by user
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Otherwise redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Return to results page when voting post is successfully performed
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
