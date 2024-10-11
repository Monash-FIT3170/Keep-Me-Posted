from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Meeting
from .serializers import MeetingSerializer

# View to create a meeting
class MeetingCreateView(APIView):
    def post(self, request):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve meetings for a user
class MeetingRetrieveView(generics.ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        email = self.kwargs['user_email']  # Ensure this matches your URL pattern
        return Meeting.objects.filter(user_email=email)
