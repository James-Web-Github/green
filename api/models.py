from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    quantity  = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    thumbnail = models.ImageField(upload_to='products/thumbnails/',null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name