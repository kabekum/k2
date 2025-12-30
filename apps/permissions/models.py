from django.db import models
from django.conf import settings
from apps.matters.models import Matter

User = settings.AUTH_USER_MODEL

class MatterPermission(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('lawyer', 'Lawyer'),
        ('staff', 'Staff'),
        ('viewer', 'Viewer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('user', 'matter')
