from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    question_text = RichTextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.question_text
    
    def get_absolute_url(self):
        return reverse('question_detail', kwargs = {'pk': self.pk})

class Answer(models.Model):
    answer_text = RichTextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.answer_text