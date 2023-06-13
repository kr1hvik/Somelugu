from django.shortcuts import render
from django.http import HttpResponse
from .models import Tekst
from django.shortcuts import render, get_object_or_404
from .models import Tekst
import markdown



def home(request):
    return render(request, "homepage/main.html") #homepagele saamine

def vaatamine(request, title):
    tekst = get_object_or_404(Tekst, title=title)

    # loeb markdowni file contenti sisse
    markdown_content = ""
    if tekst.dokument:
        with tekst.dokument.open() as file:
            markdown_content = file.read().decode('utf-8')

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    return render(request, 'homepage/vaata.html', {'tekst': tekst, 'html_content': html_content})

def dino(request):
    return render(request, 'homepage/dino.html', {})
