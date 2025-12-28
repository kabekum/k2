from django.db import models
from django.conf import settings
from apps.matters.models import Matter

class TimeEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    billable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
