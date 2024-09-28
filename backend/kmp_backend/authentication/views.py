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
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import smtplib, ssl, markdown2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from django.conf import settings


@api_view(['POST'])
def send_password_reset(request):
    try:
        user = User.objects.get(email=request.POST.get("email"))
        
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user:
        username =  os.getenv("SMTP_EMAIL")
        password = os.getenv("SMTP_API_KEY")        
        
        email = MIMEMultipart("alternative")
        email["Subject"] = "KMP Password Reset"
        email["From"] = os.getenv("SMTP_EMAIL")
        email["To"] = request.POST.get("uid")
        
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token_generator = PasswordResetTokenGenerator()
        token = urlsafe_base64_encode(force_bytes(token_generator.make_token(user=user)))
        reset_link = settings.FRONTEND_URL + f"/reset_password/{uid}/{token}"
        
        message = f"""
Hello,

We received a request to reset the password for your account associated with this email address. If you made this request, you can reset your password by clicking the link below:

[Reset Your Password]({reset_link})

If you didn’t request a password reset, you can safely ignore this email. Rest assured, your account is safe.

---

### What Happens Next?
After clicking the link, you'll be redirected to a page where you can enter a new password. This link will expire in **10 minutes** for your security. If you need a new link, please submit a new password reset request.

Thank you,  
The **Keep Me Posted** Team

---

If you’re having trouble clicking the "Reset Your Password" button, copy and paste the following URL into your web browser:

`{reset_link}`
        """
        
        part1 = MIMEText(message, "plain")

        message_html = markdown2.markdown(message)
        part2 = MIMEText(message_html, "html")
    
        email.attach(part1)
        email.attach(part2)
        
        try:
            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(username, password)
                server.sendmail(
                    username, user.email, email.as_string()
                )
            
            return Response("Email sent successfully", status=200)
        except:
            pass
        
    return Response("Email did not send", status=500)

@api_view(['POST'])
def reset_password(request):   
    try:
        user_id = urlsafe_base64_decode(request.POST.get("uid")).decode()
        user = User.objects.get(pk=user_id)
        
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user and default_token_generator.check_token(user, urlsafe_base64_decode(request.POST.get("token")).decode()):
        user.set_password(request.POST.get("password"))
        user.save()
        return Response("Password reset", status=200)
    
    return Response("Invalid token", status=400)
        
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