from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.matters.models import Matter
from apps.matters.serializers import MatterSerializer

class ClientMattersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'client':
            return Response(status=403)

        matters = Matter.objects.filter(client__email=request.user.email)
        serializer = MatterSerializer(matters, many=True)
        data = [{"id": m.id, "title": m.title, "status": m.status} for m in matters]
       return Response(serializer.data)

