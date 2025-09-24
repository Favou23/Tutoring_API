from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .searializers import RegisterSerializer, LogoutSerializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from accounts.tasks import send_welcome_email


User = get_user_model()

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email, user.username)
    
class Logout (generics.GenericAPIView):
    serializer_class = LogoutSerializers
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        try:
            
            refresh_token = serializer.validated_data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response ({'message': "Successfuly logged out"}, status= status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response ({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            # Here you would generate a password reset token and send an email
            # For simplicity, we'll just simulate this process
            reset_token = "dummy-reset-token"  # Replace with actual token generation logic
            # Send email logic goes here
            return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)
