from rest_framework import generics

# Serializers
from product.serializers.product import ProductSerializer

# Models
from product.models import Product


class ProductListView(generics.ListAPIView):
	'''List all products'''
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
	'''Return Detail Product'''
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class FeaturedProductListView(generics.ListAPIView):
	'''All featured products'''
	queryset = Product.objects.filter(status='featured')
	serializer_class = ProductSerializer


class NewProductListView(generics.ListAPIView):
	'''All new-arrivals products'''
	queryset = Product.objects.filter(status='new_arrivals')
	serializer_class = ProductSerializer