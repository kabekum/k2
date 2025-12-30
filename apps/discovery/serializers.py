from rest_framework.serializers import ModelSerializer
from .models import Evidence

class EvidenceSerializer(ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'
