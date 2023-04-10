from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterAPIView, UserLoginView, UserUpdateView

app_name = 'users'

urlpatterns = [
    path('api/v1/registration/', RegisterAPIView.as_view(), name='registration_user'),
    path('api/v1/login/', UserLoginView.as_view(), name='login_user'),
    path('api/v1/update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]