from django.urls import path
from quora.views import index, makeQuestion, signIn, QuestionDetail
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='quora'),
    path('question_detail/<int:pk>/', QuestionDetail.as_view(), name='QuestionDetail'),
    path('make_question/', makeQuestion, name='makeQuestion'),
    path('sign_in/', signIn, name = 'signIn')
    ]
