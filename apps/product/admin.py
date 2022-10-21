from django.contrib import admin

from .models import Category, Brand, Product, Rating, Image
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)


class InlineRating(admin.StackedInline):
	model = Rating
	extra = 1


class InlineImage(admin.StackedInline):
	model = Image
	extra = 0
	min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	inlines = (
		InlineImage,
		InlineRating
	)