from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ('email', 'username', 'phone', 'is_active')
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('phone',)}),
	)


admin.site.register(CustomUser, CustomUserAdmin)