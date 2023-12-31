from django.db import models
from api.category.models import Category
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False, blank=True)
    image=models.ImageField(upload_to='images/', null = True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name  