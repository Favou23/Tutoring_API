from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .searializers import RegisterSerializer, LogoutSerializers,ResetPasswordRequestSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from accounts.tasks import send_welcome_email
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from .searializers import SetNewPasswordSerializer
from .tasks import send_password_reset_email, send_password_reset_success_email

# from django.contrib.auth import default_token_generator



User = get_user_model()
token_generator = PasswordResetTokenGenerator()

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


class RequestPasswordReset(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ResetPasswordRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data["email"]
        user = User.objects.filter(email=email).first()
        
        if user :
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            reset_link =  f"http://localhost:8000/api/reset-password-confirm/{uid}/{token}/"
            send_password_reset_email.delay(email, reset_link)
        return Response({"message": "if the email exixsts, a reset link has been sent."})
    
    
class ResetPassword(APIView):
    permission_classes = [AllowAny]
    def post(self, request, uidb64,token):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            
            if not token_generator.check_token(user,token):
                return Response ({"error": "Invalid or expired token"}, status=400)

            user.set_password(serializer.validated_data["password"])
            user.save()
            send_password_reset_success_email.delay(user.email)
            return Response({"message": "password reset successful"} )
        except Exception as e:
            return Response({"error": "Invalid Request"}, status=400)
