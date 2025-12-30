from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from .models import TrustLedger, TrustTransaction


def generate_trust_ledger_report(ledger: TrustLedger, file_path: str):
    c = canvas.Canvas(file_path, pagesize=LETTER)
    text = c.beginText(40, 750)

    text.textLine(f"Client Trust Ledger: {ledger.client.name}")
    text.textLine(f"Current Balance: {ledger.balance}")
    text.textLine("")

    transactions = TrustTransaction.objects.filter(ledger=ledger).order_by('created_at')

    for tx in transactions:
        text.textLine(
            f"{tx.created_at.date()} | {tx.transaction_type.upper()} | "
            f"{tx.amount} | {tx.description}"
        )

    c.drawText(text)
    c.save()
