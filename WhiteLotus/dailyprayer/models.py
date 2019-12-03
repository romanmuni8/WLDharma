from django.core.exceptions import ValidationError
from django.db import models


class Practice(models.Model):
    number = models.IntegerField()
    text = models.TextField()


class DailyPracticeManager(models.Manager):
    def create_daily_practice(self, chosen, choose_date):
        dp = self.create(chosen=chosen, choose_date=choose_date)
        return dp


class DailyPractice(models.Model):
    chosen = models.ForeignKey(Practice, on_delete=models.SET_NULL, null=True)
    choose_date = models.DateField()

    objects = DailyPracticeManager()

    def save(self, *args, **kwargs):
        if not self.pk and DailyPractice.objects.exists():
            raise ValidationError('There is can be only one Daily Practice instance')
        return super(DailyPractice, self).save(*args, **kwargs)
