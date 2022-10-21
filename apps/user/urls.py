from django.urls import path
from rest_framework_simplejwt.views import (
	TokenRefreshView,
)

from .views import views


urlpatterns = [
	path('signup/', views.sign_up, name="sign_up"),
	path('signin/', views.sign_in, name="sign_in"),
	path('signout/', views.sign_out, name="sign_out"),
	path('confirm/', views.confirm, name='confirm'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]