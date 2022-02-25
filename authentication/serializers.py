from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True, min_length=4,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, min_length=6, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, min_length=6, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=4, required=True)
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'password']
