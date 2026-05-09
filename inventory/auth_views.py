from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    # Email restriction logic: Only emails containing "tms" are allowed
    if "tms" not in email.lower():
        return Response({"error": "Registration restricted to 'tms' authorized emails only."}, status=status.HTTP_403_FORBIDDEN)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
