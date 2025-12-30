from django.db import models
from apps.matters.models import Matter

class Evidence(models.Model):
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='evidence/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
