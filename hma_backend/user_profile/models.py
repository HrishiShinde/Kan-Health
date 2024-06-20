from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    health_history = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
