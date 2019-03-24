from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length = 500)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) ## 'Author'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('QuestionDetail', args=[str(self.id)])
    
##class Author(models.Model):
##    user = models.OneToOneField(User, on_delete.SET_NULL, null = True, primary_key=True)

class Answer(models.Model):
    content = models.TextField(null = True)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) ## 'Author'
    question = models.ForeignKey(Question, on_delete = models.CASCADE, null=True)

##class Tag(models.Model):
##    tag = models.CharField(max_length = 25)
##    question = models.ManyToManyField(Question, on_delete=models.SET_NULL, null=True)
    
