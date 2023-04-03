from django.urls import path
from .views import RegisterAPIView

app_name = 'users'

urlpatterns = [
    path('api/v1/registration/', RegisterAPIView.as_view(), name='registration_user'),
]