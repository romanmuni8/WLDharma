from django.db import models


class Practice(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=None)


class DailyPractice(models.Model):
    chosen = models.ForeignKey(Practice, on_delete=models.SET_NULL(), null=True)
    choose_date = models.DateField()
