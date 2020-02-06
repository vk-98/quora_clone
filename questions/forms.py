from django import forms
from .models import Question, Answer

class NewQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_text']
        widgets = { 'question_text': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super(NewQuestionForm, self).__init__(*args, **kwargs)