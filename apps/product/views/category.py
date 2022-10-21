from rest_framework import generics

# Serializers
from product.serializers.category import CategorySerializer

# Models
from product.models import Category


class CategoryListView(generics.ListAPIView):
	'''List all categories'''
	queryset = Category.objects.all()
	serializer_class = CategorySerializer