from rest_framework import serializers
from .models import TrustAccount, TrustLedger, TrustTransaction


class TrustAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustAccount
        fields = '__all__'


class TrustLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustLedger
        fields = '__all__'


class TrustTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustTransaction
        fields = '__all__'
        read_only_fields = ('performed_by', 'created_at')
