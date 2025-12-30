from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.matters.views import MatterViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from apps.discovery.views import EvidenceViewSet


router = DefaultRouter()
router.register('matters', MatterViewSet)
router.register(r'discovery/evidence', EvidenceViewSet, basename='evidence')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('apps.trust.urls')),
    path('api/portal/matters/', ClientMattersView.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),



]
