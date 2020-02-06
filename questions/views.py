from django.shortcuts import render
from .models import Question, Answer
from .forms import NewQuestionForm
# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }
    return render(request, 'questions/home.html', context)

def create(request):
    form = NewQuestionForm()
    context = {
        'form': form
    }
    return render(request, 'questions/create.html', context)