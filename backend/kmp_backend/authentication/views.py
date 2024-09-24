from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# views.py
from django.contrib.auth.views import PasswordResetView
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        """
        Override the method to include a custom URL for the frontend in the password reset email.
        """
        current_site = get_current_site(self.request)
        email_template_name = 'registration/password_reset_email.html'

        # Get the frontend URL
        frontend_url = settings.FRONTEND_URL

        # Generate the token and other details
        form.save(
            domain_override=current_site.domain,
            use_https=self.request.is_secure(),
            email_template_name=email_template_name,
            extra_email_context={
                'frontend_url': frontend_url
            },
            request=self.request
        )
        return super().form_valid(form)

@api_view(['POST'])
def login(request):
    """
    Endpoint for user login.

    This view receives a POST request with user credentials (email and password).
    It checks if the provided credentials are valid and returns a token if authentication is successful.

    Args:
        request (HttpRequest): The incoming HTTP request object containing user credentials.

    Returns:
        Response: JSON response with authentication token and user details if authentication is successful,
                  or an error message with HTTP status code if authentication fails.
    """
    # Check if email or password is missing
    if 'email' not in request.data or request.data['email'] == "":
        return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
    if 'password' not in request.data or request.data['password'] == "":
        return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_object_or_404(User, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found!"}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    """
    Endpoint for user registration.

    This view receives a POST request with user details (username, email, and password).
    It checks if the provided email is already in use, and if not, registers the user and returns a token.

    Args:
        request (HttpRequest): The incoming HTTP request object containing user details.

    Returns:
        Response: JSON response with authentication token and user details if registration is successful,
                  or an error message with HTTP status code if registration fails.
    """    
    # Check if email is already in use
    if User.objects.filter(email=request.data['email']).exists():
        return Response({"error": "This email address is already in use."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])

        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    # Return error if serializer data is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    """
    Test endpoint for token authentication.

    This view is protected and requires a valid authentication token to access.
    It returns a simple message confirming successful token-based authentication.

    Args:
        request (HttpRequest): The incoming HTTP request object containing authentication token.

    Returns:
        Response: JSON response with a success message indicating successful token authentication.
    """
    return Response("passed for {}".format(request.user.email))