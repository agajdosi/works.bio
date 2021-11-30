from django.db import models

# Create your models here.

class Artwork(models.Model):
  title = models.CharField(max_length=100)
  created = models.DateField('created')
  about = models.CharField(max_length=800)
  previewFile = models.FileField()

