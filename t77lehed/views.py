from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponse
from .models import Image
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
    file_path = 'path/to/file.docx'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("File not found")

# Create your views here.

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