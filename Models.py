# models.py
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
