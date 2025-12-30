from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('lawyer', 'Lawyer'),
        ('staff', 'Staff'),
        ('client', 'Client'),
    ]
    firm = models.ForeignKey('firms.Firm', on_delete=models.CASCADE, null=True)
    office = models.ForeignKey('firms.Office', on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
