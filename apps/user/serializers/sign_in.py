from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404

from user.models import CustomUser


class SignInSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=68,
        min_length=6,write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)
    tokens = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'tokens')

    def get_tokens(self, obj):
        user = get_object_or_404(CustomUser, email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def get_username(self, obj):
        user = get_object_or_404(CustomUser, email=obj['email'])
        if user.username is not None:
            return user.username

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }