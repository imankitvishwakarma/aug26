from django.db import models
from tinymce.models import HTMLField

class service(models.Model):
    service_icon=models.CharField(max_length=30)
    service_heading=models.CharField(max_length=30)
    service_details=models.CharField(max_length=30)

# Create your models here.
