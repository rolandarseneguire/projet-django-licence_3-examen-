from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
      path('index.html', views.index, name='index'),  # page d’accueil
    path('questionnaire.html', views.questionnaire, name='questionnaire'),  # page du questionnaire
]