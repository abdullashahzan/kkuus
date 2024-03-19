from .models import *
from datetime import datetime, timedelta
from firebase_admin import storage
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import string
import secrets

def generate_random_key():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(6))

def send_email(subject, recipient_list, title, body, special_keys):
    subject = subject
    from_email = 'kkuunofficialstore@gmail.com'
    recipient_list = recipient_list
    html_content = render_to_string('email_template.html', {'Title': title, 'Body': body, 'specialKeys':special_keys})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    email.attach_alternative(html_content, "text/html")
    try:
        email.send()
        return f"success"
    except:
        return f"failed"

def get_user_wishlist(username):
    wishlist = UserWishlist.objects.get(username=username)
    wishlist_items = wishlist.item.filter(is_expired=False)
    return wishlist_items

def delete_image(firebase_path):
    firebase_path = f'product_images/{firebase_path}/'
    firebase_bucket = storage.bucket()
    try:
        blob = firebase_bucket.blob(firebase_path)
        blob.delete()
        return "success"
    except Exception as e:
        return f"Error deleting image '{firebase_path}': {str(e)}"

def delete_listing(listing_id):
    listing_details = UserListings.objects.get(id=listing_id)
    delete_image(listing_details.firebase_path)
    listing_details.delete()
    return

def check_data():
    current = datetime.now()
    long_current = datetime.now() - timedelta(days=10)
    expired_objects = UserListings.objects.filter(expiry__lt=current, is_expired=False)
    for obj in expired_objects:
        obj.is_expired = True
        obj.save()

def set_expiry(days):
    current_datetime = datetime.now()
    expiry_date = current_datetime + timedelta(days=int(days))
    return expiry_date

def num_buyers(item_id):
    item = UserListings.objects.get(id=item_id)
    orders = UserOrder.objects.filter(item=item).count
    return orders

def generate_notification(title, body, username):
    notification = UserNotification(title=title, body=body,  username=username).save()
