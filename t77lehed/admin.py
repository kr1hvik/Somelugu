from django.contrib import admin
from .models import image

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(image, imageAdmin)