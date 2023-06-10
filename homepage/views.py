from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Tekst
from django.shortcuts import render
from docx import Document
from django.template.defaultfilters import linebreaksbr
from .models import Tekst
import markdown


def koristatud(request):
    

    koristatud=[]
    failid = [tekst.dokument.name for tekst in Tekst.objects.all()]
    for f in failid:
        puhas=""
        for s in f:  
            if s == "_":
                break
            puhas+=s
        #{% url 'vaatamine' %}
        koristatud.append([puhas, "{%url'"+f+"'%}" ])#+domain+"/"
    return koristatud

def home(request):
    domain = request.build_absolute_uri('/')[:-1]
    return render(request, "homepage/main.html", {"lehed":koristatud(request), "BASE_DIR":domain}) 


def realica(request, leht):
    domain = request.build_absolute_uri('/')[:-1]
    dok=leht[6:-3]
    number=Tekst.objects.get(dokument=str(dok)).id
    tekst_instance = Tekst.objects.get(id=number)
    saved_file = tekst_instance.dokument


    if saved_file.name.endswith('.docx'):
        doc= Document(saved_file)
        paragraphs= [paragraph.text for paragraph in doc.paragraphs]
        return render(request, 'homepage/realica.html', {'sisu': paragraphs, "lehed":koristatud(request), "current":dok[0:-5], "BASE_DIR":domain})
    else:
        with saved_file.open() as file:
            file_content = file.read().decode("utf-8")
            file_content = linebreaksbr(file_content)
        return render(request, "homepage/realica.html", {"sisu":file_content, "lehed":koristatud(request), "current":dok[0:-3], "BASE_DIR":domain})



def vaatamine(request, tekst_id):
    tekst = Tekst.objects.get(id=tekst_id)

    # Read the content of the uploaded file
    markdown_content = ""
    if tekst.dokument:
        with tekst.dokument.open() as file:
            markdown_content = file.read().decode('utf-8')

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    return render(request, 'homepage/vaata.html', {'tekst': tekst, 'html_content': html_content})
