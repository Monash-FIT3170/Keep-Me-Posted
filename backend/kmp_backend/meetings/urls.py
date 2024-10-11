from django.urls import path
from .views import MeetingCreateView, MeetingRetrieveView

urlpatterns = [
    path('', MeetingCreateView.as_view(), name='meeting-create'),  # For POST
    path('<str:user_email>/', MeetingRetrieveView.as_view(), name='meeting-retrieve'),  # For GET
]
