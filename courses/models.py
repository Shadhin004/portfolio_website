from django.db import models


class experience(models.Model):
    title=models.CharField(max_length=255)
    duration=models.CharField(max_length=255)
    description=models.CharField(max_length=10055)
    image=models.FileField(upload_to='courses/static', blank=True)

