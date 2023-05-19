from django.urls import path
from .views import  view_docx, view_pdf, pildid

urlpatterns = [
    #path('töölehed/', gallery, name="gallery"),
    path("docx/", view_docx, name="docx"),
    path("pdf/", view_pdf, name="pdf"),
    path("pildid/", pildid,  name="pildid"),
]