from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import NewQuestionForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }
    return render(request, 'questions/home.html', context)


class QuestionCreationView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_text']

    class Meta:
        widgets = { 'question_text': forms.TextInput()}
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnswerCreationView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer_text']
    class Meta:
        widgets = { 'answer_text': forms.TextInput()}
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionDetailView(DetailView):
    model = Question