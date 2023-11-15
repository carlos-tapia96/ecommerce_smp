from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer

# Create your models here.

# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.name

# PRODUCT
class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='products/images',null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def image_URL_check(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url