from django.db import models

class NetworkData(models.Model):
    location = models.CharField(max_length=100)
    signal_strength = models.IntegerField()

    def __str__(self):
        return self.location
