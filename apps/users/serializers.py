from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone_number', 'password', 'email',
            'username', 'first_name', 'last_name',
            'location', 'birth_date', 'gender'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user
