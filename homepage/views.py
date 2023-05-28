from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Tekst
from django.shortcuts import render
from docx import Document

def home(response):
    return render(response, "homepage/main.html", {}) 
def realica(request):
    return render(request, "homepage/realica.html")
def upload_file(request):
    if request.method == 'POST':
        form= UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse ("file nimi on ")
    else: 
        form= UploadFileForm()
    return render(request, 'homepage/upload.html', {'form': form})
def vaatamine(request):
    tekst_instance = Tekst.objects.get(id= 7)
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