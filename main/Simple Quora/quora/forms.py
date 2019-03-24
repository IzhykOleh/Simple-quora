from django.forms import ModelForm
from quora.models import Question, Answer
from django import forms

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        
