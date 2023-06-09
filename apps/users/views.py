import base64
from io import BytesIO
import qrcode
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework import status, serializers
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from random import randint
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer, QRSerializer

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    """Регистрация пользователей"""

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


class UserLoginView(APIView):
    """Вход для пользователей"""
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        phone_number = data['phone_number']
        password = data['password']

        user = User(phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError({'detail': 'Incorrect phone or password'})

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            , status=status.HTTP_200_OK
        )


class UserUpdateView(generics.UpdateAPIView):
    """Изменение данных пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # def get_object(self):
    #     return self.request.user


class UserDetailView(APIView):
    """
    Получить информацию о текущем пользователе по ссылке QR кода
    """
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserQRView(APIView):
    """
    Получить QR код-ссылку о пользователе
    """
    def get(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not request.user.phone_number:
            return Response({'detail': 'User phone is not provided.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = QRSerializer(request.user)
        try:
            user_url = request.build_absolute_uri(reverse('users:user_detail', kwargs={'pk': request.user.id}))
        except NoReverseMatch:
            return Response({'detail': 'Invalid URL.'}, status=status.HTTP_400_BAD_REQUEST)
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(user_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        buffered.seek(0)
        qr_code_base64 = base64.b64encode(buffered.read()).decode("utf-8")
        data = {
            'user': serializer.data,
            'qr_code': qr_code_base64
        }
        return render(request, 'qr_code.html', data)

# class ResetPasswordRequestView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         email = request.data.get('email')
#         if email:
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
#             # generate 4-digit code
#             code = randint(1000, 9999)
#             # save code to user profile
#             user.reset_password_code = code
#             user.save()
#             # send email with code
#             subject = 'Password reset code'
#             message = f'Your password reset code is: {code}'
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [email]
#             send_mail(subject, message, email_from, recipient_list)
#             return Response({'success': 'Code sent to email'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ResetPasswordConfirmView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         email = request.data.get('email')
#         code = request.data.get('code')
#         password = request.data.get('password')
#         if email and code and password:
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
#             if user.profile.reset_password_code == int(code):
#                 # reset password
#                 user.set_password(password)
#                 user.reset_password_code = None
#                 user.save()
#                 # generate new JWT token
#                 refresh = RefreshToken.for_user(user)
#                 response_data = {
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 }
#                 return Response({'success': 'Password reset successfully', 'tokens': response_data}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Email, code, and password are required'}, status=status.HTTP_400_BAD_REQUEST)
