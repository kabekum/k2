from django.db import models
from django.conf import settings
from apps.clients.models import Client
from apps.matters.models import Matter

User = settings.AUTH_USER_MODEL


class TrustAccount(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]

    name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='USD')
    is_iolta = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TrustLedger(models.Model):
    trust_account = models.ForeignKey(
        TrustAccount,
        on_delete=models.CASCADE,
        related_name="ledgers"
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    class Meta:
        unique_together = ('trust_account', 'client')

    def __str__(self):
        return f"{self.client.name} Ledger"


class TrustTransaction(models.Model):
    TRANSACTION_TYPE = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    ledger = models.ForeignKey(TrustLedger, on_delete=models.CASCADE)
    matter = models.ForeignKey(Matter, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
