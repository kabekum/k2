from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .summarizer import summarize_text

class DocumentSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get('text')
        summary = summarize_text(text)
        return Response({'summary': summary})
