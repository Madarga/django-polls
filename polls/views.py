from django.http import HttpResponse
from django.template import loader

from .models import Question 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   #object from the beginning to position 5 (excluded), '-pub_date' means the order is reverse  
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)  #'%s' indicates the value of question_id

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)