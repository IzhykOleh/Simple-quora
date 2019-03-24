from django.contrib import admin
from .models import Question, Answer

models_for_registration = [
    Question,
    Answer,
    ]

for m in models_for_registration:
    admin.site.register(m)
