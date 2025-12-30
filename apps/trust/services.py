from decimal import Decimal
from django.core.exceptions import ValidationError
from apps.billing.models import Invoice
from .models import TrustLedger, TrustTransaction


class TrustToInvoiceService:

    @staticmethod
    def apply_trust_payment(invoice: Invoice, amount: Decimal, user):
        ledger = TrustLedger.objects.get(client=invoice.client)

        if ledger.balance < amount:
            raise ValidationError("Insufficient trust funds")

        # Withdraw from trust
        TrustTransaction.objects.create(
            ledger=ledger,
            matter=invoice.matter,
            transaction_type='withdrawal',
            amount=amount,
            description=f"Applied to Invoice #{invoice.id}",
            performed_by=user
        )

        # Apply payment to invoice
        invoice.amount_paid += amount
        invoice.save()
