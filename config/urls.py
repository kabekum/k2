from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.matters.views import MatterViewSet

router = DefaultRouter()
router.register('matters', MatterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
