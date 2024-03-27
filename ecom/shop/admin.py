from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserListings)
admin.site.register(UserWishlist)
admin.site.register(UserOrder)
admin.site.register(UserComment)
admin.site.register(UserNotification)
admin.site.register(UserProfile)
admin.site.register(FCMToken)