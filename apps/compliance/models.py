from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    object_id = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.timestamp} - {self.action}"
