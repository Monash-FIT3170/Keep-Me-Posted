from django.core.files.storage import FileSystemStorage
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import AudioFile
from .serializers import AudioFileSerializer
from . import assemblyAI_module as TS

UPLOAD_DIRECTORY_PATH = 'assemblyaimodule/uploads/'
@api_view(['POST'])
def transcribe(request):
    serializer = AudioFileSerializer(data=request.data)
    if serializer.is_valid():
        audio_file = serializer.validated_data['audio_file']

        # Save the uploaded file locally
        fs = FileSystemStorage(location=UPLOAD_DIRECTORY_PATH)
        saved_file = fs.save(audio_file.name, audio_file)

        # Get the URL of the saved file within the app directory
        saved_file_url = UPLOAD_DIRECTORY_PATH + saved_file

        # Call the transcribe function with the file URL
        transcription = TS.transcribe(saved_file_url)
        transcription_with_speakers = TS.transcribe_with_speakers(saved_file_url)

        # Delete the file after transcription (optional)
        fs.delete(saved_file)

        return Response({
            'transcription': transcription,
            'transcription_with_speakers': transcription_with_speakers
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def transcribe_with_speakers(request):
    serializer = AudioFileSerializer(data=request.data)
    if serializer.is_valid():
        audio_file = serializer.validated_data['audio_file']

        # Save the uploaded file locally within the "assemblyaimodule" app
        fs = FileSystemStorage(location=UPLOAD_DIRECTORY_PATH)
        saved_file = fs.save(audio_file.name, audio_file)

        # Get the URL of the saved file within the app directory
        saved_file_url = UPLOAD_DIRECTORY_PATH + saved_file

        # Call the transcribe function with the file URL
        transcription = TS.transcribe_with_speakers(saved_file_url)

        # Delete the file after transcription (optional)
        fs.delete(saved_file)

        return Response({'transcription': transcription}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

