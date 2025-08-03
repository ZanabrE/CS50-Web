from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    imageUrl = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey("User", on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, related_name="category")


class Category(models.Model):
    name = models.CharField(max_length=64)
