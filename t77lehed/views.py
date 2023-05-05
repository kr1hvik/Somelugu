from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponse


# Create your views here.

def gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    return render(request, "template/gallery.html", {"form": form})