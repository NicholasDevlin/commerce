from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Categories(models.Model):
    categoryName= models.CharField(max_length=64)

    def __str__(self):
        return self.categoryName

class Bid(models.Model):
    bid= models.IntegerField(default=0)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="userBid")


class Listing(models.Model):
    title= models.CharField(max_length=64)
    description= models.CharField(max_length=500)
    imageUrl= models.CharField(max_length=1000)
    price= models.ForeignKey(Bid, on_delete=models.CASCADE, null=True, related_name="bidPrice")
    status= models.BooleanField(default=True)
    category= models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="category")
    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    watchList= models.ManyToManyField(User, null=True, related_name="listingWatchlist")

    def __str__(self):
        return self.title 

class Comment(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, related_name="listingComment")
    message= models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user} comment on {self.listing}"

