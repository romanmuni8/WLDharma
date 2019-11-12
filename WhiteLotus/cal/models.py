from django.db import models

# adding this so when i merge this doesnt get auto deleted

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)