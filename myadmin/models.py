from django.db import models

class Category(models.Model):
	cat_name = models.CharField(max_length=100)

	class Meta:
		db_table = 'category'


class Subcategory(models.Model):
	subcategory_name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		db_table = 'subcategory'

