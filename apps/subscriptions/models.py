from django.db import models
from apps.firms.models import Firm

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    max_users = models.IntegerField()
    max_matters = models.IntegerField()


class Subscription(models.Model):
    firm = models.OneToOneField(Firm, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    started_at = models.DateTimeField(auto_now_add=True)
