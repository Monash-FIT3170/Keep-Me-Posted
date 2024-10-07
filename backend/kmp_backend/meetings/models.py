# meetings/models.py

from django.db import models

class Meeting(models.Model):
    user_email = models.EmailField()
    meeting_transcript = models.TextField(default="")  # Set default to an empty string
    meeting_summary = models.TextField()
    meeting_recipients = models.JSONField(default=list)
    meeting_date = models.DateTimeField()

    def __str__(self):
        return self.meeting_transcript

