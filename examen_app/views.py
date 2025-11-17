
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'examen_app/index.html')

def questionnaire(request):
    now=datetime.now()
    return render(request, 'examen_app/questionnaire.html',{'now':now})