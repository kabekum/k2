from django.db import models
from apps.clients.models import Client
from django.conf import settings

class Matter(models.Model):
    STATUS = [
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('pending', 'Pending'),
    ]

    PRIORITY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(max_length=20, choices=STATUS)
    priority = models.CharField(max_length=20, choices=PRIORITY)
    opened_at = models.DateTimeField(auto_now_add=True)
