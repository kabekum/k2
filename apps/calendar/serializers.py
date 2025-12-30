from rest_framework.serializers import ModelSerializer
from .models import CourtEvent

class CourtEventSerializer(ModelSerializer):
    class Meta:
        model = CourtEvent
        fields = '__all__'
