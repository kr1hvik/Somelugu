from django.urls import path
from .views import  pildid

urlpatterns = [
    path("pildid/", pildid,  name="pildid"),
]