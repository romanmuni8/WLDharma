from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)


class Images(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE())
    image = models.ImageField()