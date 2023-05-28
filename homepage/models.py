from django.db import models

class Tekst(models.Model):
    dokument = models.FileField(null=True)
   
