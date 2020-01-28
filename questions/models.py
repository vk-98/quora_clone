from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer_text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.answer_text