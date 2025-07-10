from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
