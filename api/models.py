from django.db import models

class Category(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=10)

class Product(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.TextField(max_length=2)
    picture = models.TextField()
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)