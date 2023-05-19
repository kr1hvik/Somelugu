from django.db import models

class image(models.Model):
    title = models.CharField(max_length=20,default='0000000')
    photo = models.ImageField(upload_to='media',default='0000000')