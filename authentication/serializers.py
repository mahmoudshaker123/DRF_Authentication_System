from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

        def create(self , validated_data):
            user = User(
                email = validated_data['email'],
                username = validated_data['username'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']

            )

            user.set_password(validated_data['password'])
            user.save()
            return user
    