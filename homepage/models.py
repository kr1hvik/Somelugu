from django.db import models

class Tekst(models.Model):
    title = models.CharField(max_length=100, null=True)
    dokument = models.FileField(null=True)
   
