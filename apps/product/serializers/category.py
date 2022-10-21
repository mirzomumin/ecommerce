from rest_framework import serializers

from product.models import Category


class CategorySerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Category
		fields = ('id', 'name', 'parent', 'image')

	def get_image(self, obj):
		return obj.image.url