from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import CourtEvent
from .serializers import CourtEventSerializer

class CourtEventViewSet(ModelViewSet):
    queryset = CourtEvent.objects.all()
    serializer_class = CourtEventSerializer
    permission_classes = [IsAuthenticated]
