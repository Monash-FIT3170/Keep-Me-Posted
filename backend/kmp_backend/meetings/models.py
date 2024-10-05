# meetings/models.py

from django.db import models

class Meeting(models.Model):
    user_email = models.EmailField()
    meeting_string = models.TextField()
    meeting_date = models.DateTimeField()

    def __str__(self):
        return self.meeting_string
