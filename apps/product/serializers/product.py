from rest_framework import serializers

from product.models import Product, Rating, Image

class ImageSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Image
		fields = ('image',)

	def get_image(self, obj):
		return obj.image.url


class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = ('stars',)


class ProductSerializer(serializers.ModelSerializer):
	category = serializers.SerializerMethodField()
	brand = serializers.SerializerMethodField()
	images = ImageSerializer(many=True)
	ratings = RatingSerializer(many=True)
	class Meta:
		model = Product
		fields = ('id', 'images', 'name', 'ratings', 'price', 'gender',
			'is_bestseller', 'status', 'category', 'brand')

	def get_category(self, obj):
		return {
			'id': obj.category.id,
			'name': obj.category.name,
			'image': obj.category.image.url
		}

	def get_brand(self, obj):
		return {
			'id': obj.brand.id,
			'name': obj.brand.name,
			'image': obj.brand.image.url
		}