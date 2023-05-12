from django.urls import path
from .views import gallery, view_docx

urlpatterns = [
    path('töölehed/', gallery, name="gallery"),
    path("docx/", view_docx, name="docx"),
]