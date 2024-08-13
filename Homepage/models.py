from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WatcheDB(models.Model):
    name = models.CharField(max_length=100) 
    description =models.TextField()
    price = models.FloatField()

    created=models.DateTimeField(auto_now_add=True),
    updated=models.DateTimeField(auto_now=True)


class watchupload(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()
    price= models.FloatField()
    image = models.ImageField(upload_to='watch_images/')
    created=models.DateTimeField(auto_now_add=True),
    updated=models.DateTimeField(auto_now=True)


class wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(watchupload)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(watchupload)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)



class Watchreviews(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ForeignKey(watchupload,on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.PositiveSmallIntegerField(choices=[(i,str(i))for i in range(1,6)])

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)