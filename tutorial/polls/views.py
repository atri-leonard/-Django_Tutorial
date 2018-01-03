from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
# A real simple index view
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))


# Returns a page with question id
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# Returns a page with question result of corresponding id
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# Returns a page with question that prompts vote options
def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)



