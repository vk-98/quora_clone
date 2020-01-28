from django.shortcuts import render
from .models import Question, Answer

# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }
    return render(request, 'questions/home.html', context)
