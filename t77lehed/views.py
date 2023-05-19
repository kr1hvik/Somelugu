from django.shortcuts import render
from .models import image


def pildid(request):
    data = image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"pilt.html", context)

from docxtpl import DocxTemplate
from django.http import HttpResponse
