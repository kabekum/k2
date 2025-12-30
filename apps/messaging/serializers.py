from rest_framework.serializers import ModelSerializer
from .models import Message

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('sender', 'created_at')
