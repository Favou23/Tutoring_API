from django.urls import path
from .views import Register, Logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/",Register.as_view(), name= 'register'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("token/refresh/",TokenRefreshView.as_view(), name= "token_refresh"),
]