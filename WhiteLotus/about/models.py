from django.core.exceptions import ValidationError
from django.db import models


class AboutPageText(models.Model):

    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and AboutPageText.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one AboutPageText instance')
        return super(AboutPageText, self).save(*args, **kwargs)


class Teacher(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    picture = models.ImageField()
