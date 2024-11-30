from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    email=models.EmailField(unique=True)



    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
    

class Product(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='image/')
    created_at=models.DateField(auto_now_add=True)
    

class Wishlist(models.Model):
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product,related_name='wishlist_product',blank=True)



        