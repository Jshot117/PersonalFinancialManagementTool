from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=50)
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    cost = models.FloatField()
    timeofexpense = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
