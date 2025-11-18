from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RequestPasswordReset, ResetPassword, Register,Logout,ProfileView,UserDetailView
urlpatterns = [
    path("register/",Register.as_view(), name= 'register'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("token/refresh/",TokenRefreshView.as_view(), name= "token_refresh"),
    path("reset-password/", RequestPasswordReset.as_view(), name="reset_password"),
    path("reset-password-confirm/<uidb64>/<token>/", ResetPassword.as_view(), name="reset_password_confirm"),
    path("users/profile/", ProfileView.as_view(), name="user_profile"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]