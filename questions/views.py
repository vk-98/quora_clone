from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Question, Answer, Thread, Tag
from .forms import NewQuestionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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
    
    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionDetailView(DetailView):
    model = Question


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

    
class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author
    

class AnswerCreationView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer_text']
    class Meta:
        widgets = { 'answer_text': forms.TextInput()}
        
    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)


class AnswerUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Answer
    fields = ['answer_text']
    pk_url_kwarg = "pk1"

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = '/'
    pk_url_kwarg = "pk1"

    def test_func(self):
        answer = self.get_object()
        return self.request.user == answer.author


        
@login_required
def vote(request, pk, pk1):

    answer = Answer.objects.get(pk = pk1)
    if Thread.objects.filter(answer = answer, userUpVoted = request.user):
        Thread.objects.filter(answer = answer, userUpVoted = request.user).delete()
    else :
        Thread.objects.create(answer = answer, userUpVoted = request.user)
    return redirect(f'/question/{pk}/')