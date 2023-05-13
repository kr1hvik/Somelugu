from django.shortcuts import render

def home(response):
    return render(response, "homepage/main.html", {}) 
def realica(request):
    return render(request, "homepage/realica.html")
