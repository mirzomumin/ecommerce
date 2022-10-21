from django.db import models

from .helpers.models import BaseModel
from user.models import CustomUser
# Create your models here.

class Category(BaseModel):
	'''Product Category'''
	parent = models.ForeignKey('self', null=True, blank=True,
		on_delete=models.CASCADE, related_name='subcategories')
	image = models.ImageField(upload_to='categories/')

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class Brand(BaseModel):
	'''Product Brand'''
	image = models.ImageField(upload_to='brands/')

	def __str__(self):
		return self.name


class Product(BaseModel):
	'''All info about product Model'''
	GENDER = (
		('men', 'Men'),
		('women', 'Women')
	)
	STATUS = (
		('featured', 'Featured'),
		('new_arrivals', 'New Arrivals'),
	)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	gender = models.CharField(max_length=10, choices=GENDER)
	status = models.CharField(max_length=15, choices=STATUS,
		blank=True, null=True)
	is_bestseller = models.BooleanField(default=False)

	# Relations
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name}'


class Image(BaseModel):
	'''Product Image'''
	name = None
	product = models.ForeignKey(Product,
		on_delete=models.CASCADE, related_name='images')
	image = models.ImageField(upload_to='products/')

	def __str__(self):
		return f'{self.product.name} {self.image.url}'


class Rating(BaseModel):
	name = None
	stars = models.PositiveSmallIntegerField()

	# Relations
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE,
		related_name='ratings')

	def __str__(self):
		return f'{self.user.username} rated\
		"{self.product.name}" on "{self.stars}"'