from django.urls import path

from .views.brand import BrandListView
from .views.category import CategoryListView
from .views.product import *


urlpatterns = [
	path('brands/', BrandListView.as_view(), name='brands'),
	path('categories/', CategoryListView.as_view(), name='categories'),
	path('all/', ProductListView.as_view(), name='all_products'),
	path('new-arrivals/', NewProductListView.as_view(), name='new_products'),
	path('featured/', FeaturedProductListView.as_view(), name='featured_products'),
	path('<int:pk>/', ProductDetailView.as_view(), name='detail_product')
]