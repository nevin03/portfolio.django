from django.db import models

# Create your models here.

class nevin(models.Model):
    Relevent_skill=models.TextField(max_length=400)
    Professional_Development=models.CharField(max_length=200)
    works=models.TextField(max_length=800)
    image=models.ImageField(upload_to="uploads")

class one(models.Model):
    name=models.TextField