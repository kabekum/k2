from django.db import models
from apps.matters.models import Matter

class Document(models.Model):
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    version = models.IntegerField(default=1)
    uploaded_at = models.DateTimeField(auto_now_add=True)
