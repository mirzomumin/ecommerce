from rest_framework import serializers

from user.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=68,
		min_length=6, write_only=True, style={'input_type': 'password'})
	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'password')


class ConfirmationCodeSerializer(serializers.Serializer):
	confirmation_code = serializers.CharField(max_length=128)