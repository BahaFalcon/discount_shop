from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone_number', 'email',
            'username', 'first_name', 'last_name',
            'location', 'birth_date', 'gender', 'avatar',
            'patronymic',
        )

        # read_only_fields = ('username', 'first_name', 'last_name', 'avatar')
        def update(self, instance, validated_data):
            user = self.context['request'].user

            if user.pk != instance.pk:
                raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

            instance.phone_number = validated_data['phone_number']
            instance.email = validated_data['email']
            instance.username = validated_data['username']
            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            instance.location = validated_data['location']
            instance.birth_date = validated_data['birth_date']
            instance.gender = validated_data['gender']
            instance.avatar = validated_data['avatar']
            instance.patronymic = validated_data['patronymic']
            instance.save()
            return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'phone_number', 'password', 'email',
            'username', 'first_name', 'last_name',
            'location', 'birth_date', 'gender', 'token'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)


class QRSerializer(serializers.ModelSerializer):
    """
    Этот сериализатор является результатом создания QR кода
    """
    id = serializers.IntegerField(default=serializers.CurrentUserDefault)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email',
            'username', 'first_name', 'last_name',
            'location', 'birth_date', 'gender', 'token'
        )

    def get_token(self, user):
        access = AccessToken.for_user(user)
        return access.token
