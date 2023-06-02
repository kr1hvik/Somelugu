from django.urls import path, re_path
from . import views
#from .views import realica

urlpatterns= [
    #re_path(r"^bio/(?P<username>\w+)/$", views.bio, name="bio"),
    path("", views.home, name= "home"),
    re_path('(?P<leht>[^/]+\.[^/]+)/$', views.realica, name='realica'),
    path("list/", views.upload_file, name="list"),
    path("vaata/", views.vaatamine,name= "vaatamine" ),
]