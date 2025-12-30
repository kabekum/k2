from django.db import models
from apps.matters.models import Matter
from django.conf import settings

User = settings.AUTH_USER_MODEL


class CourtEvent(models.Model):
    EVENT_TYPE = [
        ('hearing', 'Hearing'),
        ('deadline', 'Deadline'),
        ('trial', 'Trial'),
    ]

    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
