from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} has {self.address}"

class UserListings(models.Model):
    username = models.CharField(max_length=128)
    product_name = models.CharField(max_length=512)
    product_description = models.CharField(max_length=3000)
    product_price = models.FloatField()
    firebase_path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    expiry = models.DateTimeField(default=timezone.now)
    is_expired = models.BooleanField(default=True)
    is_renewed = models.BooleanField(default=False)
    num_raters = models.IntegerField(default=0)
    ratings = models.FloatField(default=0)
    num_orders = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} listed {self.product_name}"

class UserComment(models.Model):
    item = models.ForeignKey(UserListings, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=128)
    ratings = models.FloatField()
    heading = models.CharField(max_length=512)
    comment = models.CharField(max_length=3000)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} commented {self.heading} on {self.item.product_name}"
    
class UserWishlist(models.Model):
    username = models.CharField(max_length=128)
    item = models.ManyToManyField(UserListings, related_name="saved_items")

    def __str__(self):
        return f"{self.id} - {self.username}'s wishlist"
    
class UserOrder(models.Model):
    username = models.CharField(max_length=128)
    item = models.ForeignKey(UserListings, on_delete=models.CASCADE, related_name='orders')
    key = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} ordered {self.item.product_name}"
    
class UserNotification(models.Model):
    username = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=512)
    date = models.DateTimeField(default=timezone.now)
    task = models.CharField(max_length=20)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification {self.title} sent to {self.username}"
