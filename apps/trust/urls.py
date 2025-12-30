from rest_framework.routers import DefaultRouter
from .views import TrustAccountViewSet, TrustLedgerViewSet, TrustTransactionViewSet

router = DefaultRouter()
router.register('trust/accounts', TrustAccountViewSet)
router.register('trust/ledgers', TrustLedgerViewSet)
router.register('trust/transactions', TrustTransactionViewSet)

urlpatterns = router.urls
