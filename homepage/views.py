from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Tekst
from django.shortcuts import render
from docx import Document
from django.template.defaultfilters import linebreaksbr
from .models import Tekst
from django.conf import settings


def koristatud():
    koristatud=[]
    failid = [tekst.dokument.name for tekst in Tekst.objects.all()]
    for f in failid:
        puhas=""
        for s in f:  
            if s == "_":
                break
            puhas+=s
        #{% url 'vaatamine' %}
        koristatud.append([puhas, "{%url'"+f+"'%}" ])
    return koristatud

def home(response):
    return render(response, "homepage/main.html", {"lehed":koristatud()}) 


def realica(request, leht):
    dok=leht[6:-3]
    number=Tekst.objects.get(dokument=str(dok)).id
    tekst_instance = Tekst.objects.get(id=number)
    saved_file = tekst_instance.dokument


    if saved_file.name.endswith('.docx'):
        doc= Document(saved_file)
        paragraphs= [paragraph.text for paragraph in doc.paragraphs]
        return render(request, 'homepage/realica.html', {'sisu': paragraphs, "lehed":koristatud(), "current":dok[0:-5],"BASE_DIR":settings.BASE_DIR})
    else:
        with saved_file.open() as file:
            file_content = file.read().decode("utf-8")
            file_content = linebreaksbr(file_content)
        return render(request, "homepage/realica.html", {"sisu":file_content, "lehed":koristatud(), "current":dok[0:-3],"BASE_DIR":settings.BASE_DIR})


def upload_file(request):
    if request.method == 'POST':
        form= UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse ("file nimi on ")
        else: return HttpResponse ("error 400 ")
    else: 
        form= UploadFileForm()
    return render(request, 'homepage/upload.html', {'form': form})
def vaatamine(request):
    tekst_instance = Tekst.objects.get(id=10)
    saved_file = tekst_instance.dokument
    if saved_file.name.endswith('.docx'):
         doc= Document(saved_file)
         paragraphs= [paragraph.text for paragraph in doc.paragraphs]
         for paragraph in paragraphs:
              return HttpResponse(paragraph)
    else:
        with saved_file.open() as file:
            file_content = file.read()
            return HttpResponse(file_content)