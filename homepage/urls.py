from django.urls import path
from . import views

urlpatterns= [
    path("", views.home, name= "home"),
    path('realica/', views.realica, name='realica'),
    path('exam', views.exam, name='exam'),
    path('submit/', views.submit_exam, name='submit_exam'),
]

