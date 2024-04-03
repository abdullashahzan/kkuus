from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    building_code = models.CharField(max_length=5)
    whatsapp = models.CharField(max_length=15, null=True)
    privileged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"

class UserListings(models.Model):
    username = models.CharField(max_length=128)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=500)
    product_price = models.FloatField()
    firebase_path = models.CharField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.now)
    expiry = models.DateTimeField(default=timezone.now)
    is_expired = models.BooleanField(default=True)
    is_renewed = models.BooleanField(default=False)
    num_raters = models.IntegerField(default=0)
    ratings = models.FloatField(default=0, null=True)
    num_orders = models.IntegerField(default=0)
    new_orders = models.IntegerField(default=0)
    payment_done = models.BooleanField(default=False)
    num_views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} listed {self.product_name}"

class UserComment(models.Model):
    item = models.ForeignKey(UserListings, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=128)
    ratings = models.FloatField(null=True)
    heading = models.CharField(max_length=100, null=True)
    comment = models.CharField(max_length=200, null=True)
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
    room_no = models.IntegerField(default=0)
    building_code = models.CharField(max_length=5, default="yeah")
    whatsapp = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.username} ordered {self.item.product_name}"
    
class UserNotification(models.Model):
    username = models.CharField(max_length=128)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    task = models.CharField(max_length=20)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification {self.title} sent to {self.username}"

class FCMToken(models.Model):
    username = models.CharField(max_length=128)
    token = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} has a registered token"


class Invoice(models.Model):
    item = models.ForeignKey(UserListings, on_delete=models.CASCADE)
    invoice = models.CharField(max_length=255)

    def __str__(self):
        return f"An invoice was made: {self.invoice}"

class CroppingImageCoordinatesCache(models.Model):
    username = models.CharField(max_length=128)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"Cropping coordinates stored for {self.username}"


