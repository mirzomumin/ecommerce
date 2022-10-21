from rest_framework import generics

# Serializers
from product.serializers.brand import BrandSerializer

# Models
from product.models import Brand


class BrandListView(generics.ListAPIView):
	'''List all brands'''
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer