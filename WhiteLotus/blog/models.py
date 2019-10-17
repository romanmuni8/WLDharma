from django.db import models

# Create your models here.


class Blog(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field= None )
    text = models.CharField(max_length = 2000)