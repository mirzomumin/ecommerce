from rest_framework.decorators import (
	api_view,
	permission_classes,
	schema)
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_400_BAD_REQUEST,
	HTTP_204_NO_CONTENT)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from drf_yasg.utils import swagger_auto_schema

from user.serializers.sign_up import (
	SignUpSerializer,
	ConfirmationCodeSerializer)
from user.serializers.sign_in import SignInSerializer
from user.serializers.sign_out import SignOutSerializer
from user.models import CustomUser


@swagger_auto_schema(method='post', request_body=SignUpSerializer)
@api_view(['POST'])
def sign_up(request):
	'''Sign Up user through email and username'''
	# email = request.data.get('email')
	serializer = SignUpSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		user = serializer.save()
		user.set_password(user.password)
		user.is_active = False
		user.save()
		return Response({'response': 'Signed up successfully!'},
			status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=SignInSerializer)
@api_view(['POST'])
def sign_in(request):
	'''Sign In user through email and password'''
	serializer = SignInSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		return Response({'response': 'Success!',
			'data': serializer.data},
			status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=SignOutSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def sign_out(request):
	'''Sign Out user through refresh token'''
	serializer = SignOutSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response({'response': 'Successfully signed out!'},
			status=HTTP_204_NO_CONTENT)
	return Response({'response': 'Error'}, status=HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', query_serializer=ConfirmationCodeSerializer)
@api_view(['GET'])
def confirm(request):
	'''Confirm signed up user email'''
	code = request.query_params.get('confirmation-code')
	print(code)
	if code is not None:
		data = {'confirmation_code': code}
		serializer = ConfirmationCodeSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			code = serializer.data['confirmation_code']
			user = get_object_or_404(
				CustomUser,
				confirmation_code=code,
				verified_at=None,
				is_active=False)
			user.verified_at = now()
			user.is_active = True
			user.save()
			return Response({'response': 'Successfully Verified!'},
				status=HTTP_200_OK)
	return Response({'response': 'Bad Request'},
		status=HTTP_400_BAD_REQUEST)