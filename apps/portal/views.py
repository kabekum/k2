from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.matters.models import Matter
from apps.matters.serializers import MatterSerializer


class ClientMattersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if not hasattr(user, 'client'):
            return Response([], status=200)

        matters = Matter.objects.filter(client=user.client)
        serializer = MatterSerializer(matters, many=True)
        return Response(serializer.data)

class HealthCheckView(APIView):
    def get(self, request):
        return Response({
            "status": "ok",
            "message": "Django API is live"
        })

