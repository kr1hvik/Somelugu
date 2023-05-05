from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponse
from .models import Image
import os

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
            "BASE_DIR":os.path.dirname(os.path.dirname(__file__))
    }
    return render(request, "template/gallery.html", context)