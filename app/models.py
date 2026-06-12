from django.db import models

# Create your models here.
class EventModel(models.Model):
    event_name = models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    event_date=models.DateField()
    description=models.TextField(max_length=500)
    def __str__(self):
        return self.event_name