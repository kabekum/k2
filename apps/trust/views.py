from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import TrustAccount, TrustLedger, TrustTransaction
from .serializers import (
    TrustAccountSerializer,
    TrustLedgerSerializer,
    TrustTransactionSerializer
)
from .permissions import IsLawyerOrAdmin


class TrustAccountViewSet(ModelViewSet):
    queryset = TrustAccount.objects.all()
    serializer_class = TrustAccountSerializer
    permission_classes = [IsAuthenticated, IsLawyerOrAdmin]


class TrustLedgerViewSet(ModelViewSet):
    queryset = TrustLedger.objects.all()
    serializer_class = TrustLedgerSerializer
    permission_classes = [IsAuthenticated, IsLawyerOrAdmin]


class TrustTransactionViewSet(ModelViewSet):
    queryset = TrustTransaction.objects.all()
    serializer_class = TrustTransactionSerializer
    permission_classes = [IsAuthenticated, IsLawyerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(performed_by=self.request.user)
