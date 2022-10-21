from django.db import models

class BaseModel(models.Model):
	'''Base Model for all other Models'''

	name = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True