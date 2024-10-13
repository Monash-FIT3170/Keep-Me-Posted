from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['user_email', 'meeting_subject', 'meeting_transcript', 'meeting_summary', 'meeting_recipients', 'meeting_date']
