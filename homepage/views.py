from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Tekst
from django.shortcuts import render
from docx import Document
from django.template.defaultfilters import linebreaksbr
from .models import Tekst
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import markdown

def home(response):
    NotImplemented = [tekst.dokument.name for tekst in Tekst.objects.all()]
    return render(response, "homepage/main.html", {"lehed":nimed}) 


def realica(request, leht):
    try:
        number=Tekst(dokument=leht)

        tekst_instance = Tekst.objects.get(id=number)
        saved_file = tekst_instance.dokument
        if saved_file.name.endswith('.docx'):
            doc= Document(saved_file)
            paragraphs= [paragraph.text for paragraph in doc.paragraphs]
            return render(request, 'homepage/realica.html', {'sisu': paragraphs})
        else:
            with saved_file.open() as file:
                file_content = file.read().decode("utf-8")
                file_content = linebreaksbr(file_content)
            return render(request, "homepage/realica.html", {"sisu":file_content})
    except:
        return render(request, "homepage/realica.html", {"sisu":"Vali leht"})




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
    tekst = Tekst.objects.get(id=12)

    # Read the content of the uploaded file
    markdown_content = ""
    if tekst.dokument:
        with tekst.dokument.open() as file:
            markdown_content = file.read().decode('utf-8')

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    return render(request, 'homepage/vaata.html', {'tekst': tekst, 'html_content': html_content})
