"""
URL configuration for kmp_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for user login
    path('login', views.login, name='login'),
    # Endpoint for user signup
    path('signup', views.signup, name='signup'),
    # Test endpoint for token authentication
    path('test_token', views.test_token, name='test_token'),
    # Endpoint for sending password reset
    path('send_password_reset', views.send_password_reset, name="send_password_reset"),
    # Endpoint for retrieving the csrf token
    path('csrf', views.get_csrf_token, name='get_csrf_token')
]
