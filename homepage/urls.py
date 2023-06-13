from django.urls import path, re_path
from . import views
#from .views import realica

urlpatterns= [
    #re_path(r"^bio/(?P<username>\w+)/$", views.bio, name="bio"),
    path("", views.home, name= "home"),
    path('vaatamine/<str:title>/', views.vaatamine, name='vaatamine'),
    path("dino", views.dino, name="dino")
]