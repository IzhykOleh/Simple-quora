from django.shortcuts import render, redirect
from quora.models import Question, Answer
from quora.forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.views.generic import DetailView

def index(request):
    list_of_questions = Question.objects.all()
    title = resolve(request.path_info).url_name
    return render(request,
           'index.html',
           context = {'questions': list_of_questions,
                      'title': title,
                      }
                  )

@login_required
def makeQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user
            new_question.save()
            return redirect(reverse('quora'))
    else:
        form = QuestionForm()
        return render(request,
                  'makeQuestion.html',
                  context = {'form': form}
                  )

def signIn(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('quora'))
    else:
        form = UserCreationForm()
        return render(request,
                      'signIn.html',
                      context = {'form': form}
                      )

					  
class QuestionDetail(DetailView):
      model = Question
      template_name = 'QuestionDetail.html'
      context_object_name = 'question'
      form_class = AnswerForm

      def get_object(self):
          self.object = super().get_object() ## you have to do so because self.object doesn't exist by default
          return self.object 

      # get and post methods is called before get_context_data
      def get(self, request, *args, **kwargs):
          self.get_object() # i just need to be self.object attribute before get_context_data call, 
          form = self.form_class()
          context = self.get_context_data(**kwargs)
          context['create_answer_form'] = form
          return render(request, self.template_name, context)

      def post(self, request, *args, **kwargs):
          form = self.form_class(request.POST)
          if form.is_valid():
              answ = form.save(commit=False)
              answ.author = self.request.user
              answ.question = self.get_object()
              answ.save()
          context = self.get_context_data(**kwargs)
          context['create_answer_form'] = form
          return render(request, self.template_name, context)

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs) # self.object must be set already 
          context['answer_list'] = Answer.objects.filter(question__id = self.get_object().id)
          return context


    
