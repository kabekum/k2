from decimal import Decimal
from .models import TrustAccount, TrustTransaction


class BankReconciliationService:
    """
    Compares bank statement balance vs system balance
    """

    @staticmethod
    def calculate_system_balance(trust_account: TrustAccount) -> Decimal:
        transactions = TrustTransaction.objects.filter(
            ledger__trust_account=trust_account
        )

        balance = Decimal('0.00')
        for t in transactions:
            if t.transaction_type == 'deposit':
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    @staticmethod
    def reconcile(trust_account: TrustAccount, bank_balance: Decimal):
        system_balance = BankReconciliationService.calculate_system_balance(trust_account)

        return {
            "bank_balance": bank_balance,
            "system_balance": system_balance,
            "difference": bank_balance - system_balance,
            "status": "MATCH" if bank_balance == system_balance else "DISCREPANCY"
        }
