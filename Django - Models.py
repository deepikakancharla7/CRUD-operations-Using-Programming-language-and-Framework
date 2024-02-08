from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
