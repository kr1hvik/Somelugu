from django.shortcuts import render
#from .forms import ImageForm
from django.http import HttpResponse
from .models import image
from django.http import FileResponse
import os



""""
f = open('foobar.docx', 'rb')
document = Document(f)
f.close()

# or

with open('foobar.docx', 'rb') as f:
    source_stream = StringIO(f.read())
document = Document(source_stream)
source_stream.close()

target_stream = StringIO()
document.save(target_stream)
"""

def view_docx(request):
    filepath = f"{os.getcwd()}\\media\\kukk.pdf"
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
def view_pdf(request):
    context={
        "pdf":f"{os.getcwd()}\\media\\kukk.pdf"
    }
    return render(request, "pdf.html", context)

def pildid(request):
    data = image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)






# Create your views here.
"""
def gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    context = {
            "form": form,
            "pilt":Image.objects.get(name="jome"),
            "BASIC_DIR":os.getcwd(),
    }
    return render(request, "template/gallery.html", context)
"""