from rest_framework.viewsets import ModelViewSet
from .models import Matter
from .serializers import MatterSerializer

class MatterViewSet(ModelViewSet):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer
