from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = RichTextField()
    author = models.ForeignKey( User, on_delete = models.CASCADE )
    date_posted = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return self.question_text
    
    def get_absolute_url(self):
        return reverse('question_detail', kwargs = {'pk': self.pk})

class Answer(models.Model):
    answer_text = RichTextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='author')
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    date_posted = models.DateTimeField( default = timezone.now )

    def __str__(self):
        return self.answer_text
    
    def get_absolute_url(self):
        return reverse('question_detail', kwargs = {'pk': self.question.id})

class Tag(models.Model):
    question = models.ForeignKey( Question, on_delete = models.CASCADE )
    tag_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.tag_name

class Thread(models.Model):
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE )
    userUpVoted = models.ForeignKey( User, on_delete = models.CASCADE )

    def __str__(self):
        return f'Thread for {self.answer.id}'