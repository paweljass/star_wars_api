from django.db import models

class StarWarsData(models.Model):
    filename = models.CharField()
    data = models.JSONField()
    download_date = models.DateTimeField(auto_now_add=True)