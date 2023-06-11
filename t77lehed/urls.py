from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.quiz, name='quiz'),
    path('results/', views.submit_quiz, name='submit_quiz'),
]
