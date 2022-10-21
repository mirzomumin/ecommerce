from rest_framework import serializers

from product.models import Brand


class BrandSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Brand
		fields = ('id', 'name', 'image')

	def get_image(self, obj):
		return obj.image.url