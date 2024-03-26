from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import *
import uuid, json
def index(request):
    return render(request , 'index.html')
from firebase_admin import storage, messaging
from .scripts import *
from django.db.models import Avg
from django.conf import settings
import requests
from ecom.settings import version, FCM_Key
from pyfcm import FCMNotification

def login_user(request):
    message = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'shop:index')
            return redirect(next_url)
        else:
            message = "Invalid credentials"
    return render(request, "login.html", {"message": message})

def signup_user(request):
    message = ""
    if request.method == "POST":
        first = request.POST['first']
        second = request.POST['second']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        address = request.POST['address']
        whatsapp = request.POST['whatsapp']
        if first != "" and second != ""and email is not None and username is not None and password is not None and password2 is not None and address is not None and whatsapp != "":
            if password == password2:
                try:
                    user = User.objects.create_user(username=username, password=password)
                    user.first_name = first
                    user.last_name = second
                    user.email = email
                    user.save()
                    UserProfile(user=user, address=address, whatsapp=whatsapp).save()
                    UserWishlist(username=username).save()
                    login(request, user)
                    next_url = request.GET.get('next', 'shop:index')
                    return redirect(next_url)
                except IntegrityError:
                    message = "Username or email is already taken"
                except:
                    message = "Please make sure all the data is filled correctly"
            else:
                message = "Passwords do not match"
        else:
            message = "Please fill all the fields"
    return render(request, "signup.html", {"message": message})

def check_username_availability(request, username):
    if request.method == "POST":
        username_output = User.objects.filter(username=username).first()
        if username_output is not None:
            return JsonResponse({'response' : 'not available'})
        else:
            return JsonResponse({'response': 'available'})
        
def check_email_availability(request, email):
    if request.method == "POST":
        username_output = User.objects.filter(email=email).first()
        if username_output is not None:
            return JsonResponse({'response' : 'not available'})
        else:
            return JsonResponse({'response': 'available'})

def logout_user(request):
    logout(request)
    return redirect('shop:login_user')

def index(request):
    return HttpResponseRedirect(reverse('shop:homepage'))

def get_image(request, firebase_path):
    firebase_path = f'product_images/{firebase_path}/'
    firebase_bucket = storage.bucket()
    try:
        blob = firebase_bucket.get_blob(firebase_path)
        if blob:
            content_type = blob.content_type
            image_data = blob.download_as_bytes()
            response = HttpResponse(image_data, content_type=content_type)

            # Set cache-control headers to cache the image in the browser's cache
            response['Cache-Control'] = 'max-age=3600'  # Cache image for 1 hour (adjust as needed)
            return response
        else:
            return HttpResponse("Image not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

def homepage(request):
    check_data()
    ordered_items = UserListings.objects.filter(username=request.user.username)
    new_item_orders = 0
    for item in ordered_items:
        new_item_orders += item.new_orders
    items = UserListings.objects.filter(is_expired=False).order_by('-timestamp')
    bought_items = UserOrder.objects.filter(username=request.user.username, status='requested')
    completed_items = UserOrder.objects.filter(username=request.user.username, status='Completed')
    notifications = UserNotification.objects.filter(username=request.user.username, unread=True).count()
    cart = []
    completed = []
    for bought_item in bought_items:
        cart.append(bought_item.item.id)
    for completed_item in completed_items:
        completed.append(completed_item.item.id)
    if request.user.is_authenticated:
        user_wishlist = get_user_wishlist(request.user.username)
        user_wishlist_list = []
        for i in user_wishlist:
            user_wishlist_list.append(i.id)
        return render(request, "index.html", {"items": items, "wishlist":user_wishlist_list, "bought_items": cart, "notifications":notifications, "completed_items":completed, "new_orders": new_item_orders})
    return render(request, "index.html", {"items": items})

def notifications(request):
    ordered_items = UserListings.objects.filter(username=request.user.username)
    new_item_orders = 0
    for item in ordered_items:
        new_item_orders += item.new_orders
    notifications = UserNotification.objects.filter(username=request.user.username).order_by('-date')
    for notification in notifications:
        notification.unread = False
        notification.save()
    return render(request, "notifications.html", {"notifications": notifications, "new_orders": new_item_orders})

def delete_notification(request, notification_id):
    UserNotification.objects.get(id=notification_id).delete()
    return redirect(reverse('shop:notifications'))

def wishlist(request):
    ordered_items = UserListings.objects.filter(username=request.user.username)
    new_item_orders = 0
    for item in ordered_items:
        new_item_orders += item.new_orders
    user_wishlist = get_user_wishlist(request.user.username)
    bought_items = UserOrder.objects.filter(username=request.user.username, status='requested')
    completed_items = UserOrder.objects.filter(username=request.user.username, status='Completed')
    notifications = UserNotification.objects.filter(username=request.user.username, unread=True).count()
    user_wishlist_list = []
    cart = []
    completed = []
    for bought_item in bought_items:
        cart.append(bought_item.item.id)
    for completed_item in completed_items:
        completed.append(completed_item.item.id)
    for i in user_wishlist:
        user_wishlist_list.append(i.id)
    return render(request, "wishlist.html", {"items": user_wishlist,"wishlist":user_wishlist_list, "completed_items":completed, "bought_items": cart, "notifications":notifications, "new_orders": new_item_orders})

@login_required(login_url="shop:login_user")
def new_listing(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_description = request.POST['product_description']
        price = request.POST['price']
        plan = request.POST['flexRadioDefault']
        try:
            uploaded_file = request.FILES['product_images']
        except:
            return render(request, "sell_product.html", {"message": "Please upload the photo of your product"})
        try:
            float(price)
        except:
            return render(request, "sell_product.html", {"message": "Please type a number inside price field"})
        if product_name != "" and product_description != "" and float(price) >= 0 and uploaded_file is not None:
            unique_filename = str(uuid.uuid4())
            firebase_path = f'product_images/{unique_filename}/'
            firebase_bucket = storage.bucket()
            blob = firebase_bucket.blob(firebase_path)
            blob.upload_from_file(uploaded_file, content_type = uploaded_file.content_type)
            expiry_date = set_expiry(plan)
            UserListings(username=request.user.username, product_name=product_name, product_description=product_description, product_price=price, firebase_path=unique_filename, expiry=expiry_date, is_expired=False).save()
            notification_title = f"{product_name} was listed successfully in marketplace!"
            notification_body = f"Your product has been put up on marketplace and users are now able to see it till {expiry_date}"
            UserNotification(username=request.user.username, title=notification_title, body=notification_body, task="show_shop").save()
            return redirect(reverse('shop:homepage'))
        else:
            return render(request, "sell_product.html", {"message": "Please fill all fields"})
    else:
        return render(request, "sell_product.html")

def delete_image(firebase_path):
    firebase_path = f'product_images/{firebase_path}/'
    firebase_bucket = storage.bucket()
    try:
        blob = firebase_bucket.blob(firebase_path)
        blob.delete()
        return "success"
    except Exception as e:
        return f"Error deleting image '{firebase_path}': {str(e)}"

@login_required(login_url="shop:login_user")
def delete_listing(request, listing_id):
    listing_details = UserListings.objects.get(id=listing_id)
    delete_image(listing_details.firebase_path)
    notification_title = f"{listing_details.product_name} was removed from marketplace successfully!"
    notification_body = f"Your product is now no longer available on marketplace."
    UserNotification(username=request.user.username, title=notification_title, body=notification_body).save()
    notification_title = f"Unfortunately {listing_details.product_name} was sold to someone else"
    notification_body = f"{listing_details.product_name} has been delisted from the marketplace since it was purchased by someone else."
    all_users = UserOrder.objects.filter(item=listing_details, status="requested")
    for user in all_users:
        UserNotification(username=user.username, title=notification_title, body=notification_body).save()
    listing_details.delete()
    return redirect(reverse('shop:my_shop'))

@login_required(login_url="shop:login_user")
def my_shop(request):
    check_data()
    items = UserListings.objects.filter(username=request.user.username)
    notifications = UserNotification.objects.filter(username=request.user.username, unread=True).count()
    return render(request, 'my_shop.html', {"items": items, "notifications":notifications})

@require_POST
def add_to_wishlist(request, item_id):
    item = UserListings.objects.get(id=item_id)
    wishlist = UserWishlist.objects.get(username = request.user.username)
    wishlist.item.add(item)
    wishlist.save()
    return JsonResponse({"message": "Item added to wishlist"})

@require_POST
def remove_from_wishlist(request, item_id):
    item = UserListings.objects.get(id=item_id)
    wishlist = UserWishlist.objects.get(username=request.user.username)
    wishlist.item.remove(item)
    return JsonResponse({"message": "Item removed from wishlist"})

@require_POST
def renew_item(request, item_id):
    item = UserListings.objects.get(id=item_id)
    if item.is_renewed == False:
        item.expiry = set_expiry(1)
        item.is_renewed = True
        item.is_expired = False
        item.save()
    notification_title = f"Your product {item.product_name} was renewed for 1 day successfully!"
    notification_body = "Your product is available on the marketplace again for 1 day."
    UserNotification(username=request.user.username, title=notification_title, body=notification_body).save()
    return redirect(reverse('shop:my_shop'))

def buy(request, item_id):
    ordered_items = UserListings.objects.filter(username=request.user.username)
    new_item_orders = 0
    for item in ordered_items:
        new_item_orders += item.new_orders
    item = UserListings.objects.get(id=item_id)
    if request.user.is_authenticated:
        user_wishlist = get_user_wishlist(request.user.username)
        user_wishlist_list = []
        for i in user_wishlist:
            user_wishlist_list.append(i.id)
        comments = UserComment.objects.filter(item=item).order_by('-timestamp')
        bought_users = UserOrder.objects.filter(item=item)
        bought_users_username = []
        for i in bought_users:
            bought_users_username.append(i.username)
        user = User.objects.get(username=item.username)
        user_profile = UserProfile.objects.get(user=user)
        whatsapp = user_profile.whatsapp
        return render(request, "buy_product.html", {"item": item, "wishlist":user_wishlist_list, "comments": comments, "bought_users": bought_users_username, "whatsapp": whatsapp, "new_orders": new_item_orders})
    return render(request, "buy_product.html", {"item": item})

@require_POST
def comment(request, item_id):
    item = UserListings.objects.get(id=item_id)
    username = request.user.username
    ratings = int(request.POST['inlineRadioOptions'])
    heading = request.POST['heading']
    comment = request.POST['comment']
    if ratings is not None and heading != "" and comment != "":
        UserComment(item=item, username=username, ratings=ratings, heading=heading, comment=comment).save()
        new_avg_rating = UserComment.objects.filter(item=item).aggregate(avg_rating=Avg('ratings'))['avg_rating']
        item.ratings = format(new_avg_rating, '.2f')
        item.num_raters += 1
        item.save()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:homepage"))

@require_POST
def delete_comment(request, comment_id, item_id):
    item = UserListings.objects.get(id=item_id)
    UserComment.objects.get(id=comment_id).delete()
    new_avg_rating = UserComment.objects.filter(item=item).aggregate(avg_rating=Avg('ratings'))['avg_rating']
    item.ratings = new_avg_rating
    item.num_raters -= 1
    item.save()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:homepage"))

def order_details(request, item_id):
    item = UserListings.objects.get(id=item_id)
    purchased_by = UserOrder.objects.filter(item=item)
    details = []
    for object in purchased_by:
        user = User.objects.get(username = object.username)
        order_status = object.status
        detail = [UserProfile.objects.get(user=user), order_status]
        details.append(detail)
    return render(request, "ordered_by.html", {"item": item, "orders":details})

def purchase(request, item_id):
    item = UserListings.objects.get(id=item_id)
    buyer_object = UserProfile.objects.get(user=request.user)
    recipient_list = [User.objects.get(username=item.username).email]

    buyer_name = f"{request.user.first_name} {request.user.last_name}"
    buyer_username = request.user.username
    purchased_item = item.product_name
    purchased_item_price = item.product_price
    buyer_address = buyer_object.address
    buyer_whatsapp = buyer_object.whatsapp
    special_keys = [buyer_name, buyer_username, purchased_item, purchased_item_price, buyer_address, buyer_whatsapp]
    task = "New Order"
    message = send_email(task, recipient_list, special_keys)

    seller_user = User.objects.get(username=item.username)
    seller_object = UserProfile.objects.get(user=seller_user)

    seller_address = seller_object.address
    seller_whatsapp = seller_object.whatsapp

    if message == "success":
        key = generate_random_key()
        get_user = User.objects.get(username=item.username)
        address= UserProfile.objects.get(user=get_user).address
        whatsapp = UserProfile.objects.get(user=get_user).whatsapp
        UserOrder(username=request.user.username, item=item, key=key, status="requested", address=address, whatsapp=whatsapp).save()
        item.new_orders += 1
        item.save()
        notification_title = f"{request.user.username} would like to purchase {item.product_name}"
        notification_body = f"{buyer_name} ({buyer_username}) has ordered {purchased_item} for {purchased_item_price} SAR. Please deliver the order immediately to {buyer_address}. Contact buyer: {buyer_whatsapp}."
        UserNotification(username=item.username, title=notification_title, body=notification_body, task="show_shop").save()
        notification_title = f"Your order was placed successfully"
        notification_body = f"We have notified the seller about your order. Please wait for order acceptance from the seller. In case if the seller is not responding, here are the seller details: Whatsapp no: {seller_whatsapp}, Address info: {seller_address}"
        UserNotification(username=request.user.username, title=notification_title, body=notification_body, task="show_order").save()
        return redirect(reverse('shop:myOrders'))
    else:
        return HttpResponse("The email was not sent :(")
    
def confirm_purchase(request, item_id):
    item = UserListings.objects.get(id=item_id)
    message = ""
    if request.method == "POST":
        code = request.POST['code']
        try:
            order = UserOrder.objects.get(key=code)
        except:
            order = None
            message = "Invalid code"
        if order is not None:
            recipient_list = [User.objects.get(username=item.username).email, request.user.email]
            special_keys = [item.product_name]
            task = "Order Completed"
            try:
                message = send_email(task, recipient_list, special_keys)
            except:
                message = "Email could not be sent"
                return render(request, "confirm_purchase.html", {"item": item, "message":message})
            user = User.objects.get(username=order.username)
            notification_title = f"{item.product_name} was sold successfully to {order.username}."
            notification_body = f"Your order has been completed."
            UserNotification(username=request.user.username, title=notification_title, body=notification_body).save()
            notification_title = f"{item.product_name} was successfully purchased by you."
            UserNotification(username=order.username, title=notification_title, body=notification_body).save()
            item.new_orders -= 1
            item.num_orders += 1
            item.save()
            order.delete()
            return render(request, "purchase_complete.html", {"item":item, "user": user})
    return render(request, "confirm_purchase.html", {"item": item, "message":message})

def myOrders(request):
    ordered_items = UserListings.objects.filter(username=request.user.username)
    new_item_orders = 0
    for item in ordered_items:
        new_item_orders += item.new_orders
    notifications = UserNotification.objects.filter(username=request.user.username, unread=True).count()
    ordered_items = UserOrder.objects.filter(username=request.user.username)
    return render(request, "my_orders.html", {'orders': ordered_items, "notifications":notifications, "new_orders": new_item_orders})

def acceptOrder(request, item_id, username):
    item = UserListings.objects.get(id=item_id)
    order = UserOrder.objects.filter(username=username, item=item).first()
    order.status = "accepted"
    order.save()
    notification_title = f"Your order for {item.product_name} was accepted by {item.username}"
    notification_body = f"{item.username} has accepted your order."
    UserNotification(username=username, title=notification_title, body=notification_body).save()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:order_details"))

def rejectOrder(request, item_id, username):
    item = UserListings.objects.get(id=item_id)
    item.new_orders -= 1
    order = UserOrder.objects.filter(username=username, item=item).first()
    notification_title = f"Your order for {item.product_name} was rejected"
    notification_body = f"{item.username} has rejected your order maybe because your address was not correct or the product is out of stock."
    UserNotification(username=username, title=notification_title, body=notification_body).save()
    order.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:order_details"))

@require_POST
def search_item(request):
    ordered_items = UserListings.objects.filter(username=request.user.username)
    new_item_orders = 0
    for item in ordered_items:
        new_item_orders += item.new_orders
    item = request.POST['search']
    item = str(item).strip().lower()
    items_found = []
    all_listings = UserListings.objects.all()
    for listing in all_listings:
        cleaned_name = str(listing.product_name).strip().lower()
        cleaned_desc = str(listing.product_description).strip().lower()
        if item in cleaned_name or item in cleaned_desc:
            items_found.append(listing)
    return render(request, "search_items.html", {"items": items_found, "new_orders": new_item_orders})

@require_POST
def update_address(request):
    global address_error
    new_address = request.POST['new_address']
    object = UserProfile.objects.get(user=request.user)
    old_address = object.address
    if old_address == new_address:
        address_error = "New address cannot be the same as old address"
    elif old_address != new_address:
        object.address = new_address
        object.save()
    else:
        address_error = "An unkown error occured while changing address"
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:profile"))

def get_address():
    address = address_error
    return address

@require_POST
def update_info(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    user_object = User.objects.get(username=request.user.username)
    if first_name != "":
        user_object.first_name = first_name
        user_object.save()
    if last_name != "":
        user_object.last_name = last_name
        user_object.save()
    if email != "":
        user_object.email = email
        user_object.save()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:profile"))

@require_POST
def update_password(request):
    global password_error
    old_password = request.POST['old_password']
    new_password1 = request.POST['new_password1']
    new_password2 = request.POST['new_password2']
    if new_password1 == new_password2:
        try:
            user = User.objects.get(username=request.user.username)
            if authenticate(username=user.username, password=old_password) is not None:
                user.set_password(new_password1)
                user.save()
                logout(request)
                return redirect("shop:login_user")
            else:
                password_error = "Old password is incorrect"
        except User.DoesNotExist:
            password_error = "User does not exist"
        except Exception as e:
            password_error = "An unkown error occured."
    else:
        password_error = "New passwords do not match"
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or reverse("shop:profile"))

def get_password_error():
    err = password_error
    return err

def delete_account(request):
    username = request.user.username
    user_object = User.objects.get(username=username)
    listings = UserListings.objects.filter(username=username)
    for listing in listings:
        listing.delete()
    comments = UserComment.objects.filter(username=username)
    for comment in comments:
        comment.delete()
    wishlist = UserWishlist.objects.get(username=username)
    wishlist.delete()
    orders = UserOrder.objects.filter(username=username)
    for order in orders:
        order.delete()
    notifications = UserNotification.objects.filter(username=username)
    for notification in notifications:
        notification.delete()
    user_object.delete()
    logout(request)
    return redirect(reverse("shop:login_user"))

def profile(request):
    try:
        address_error = get_address()
    except:
        address_error = ""
    try:
        password_error = get_password_error()
    except:
        password_error = ""
    notifications = UserNotification.objects.filter(username=request.user.username, unread=True).count()
    this_user = User.objects.get(username=request.user.username)
    this_user_profile = UserProfile.objects.get(user=request.user)
    return render(request, "profile.html", {"user":this_user, "other": this_user_profile, "address_error":address_error, "password_error":password_error, "notifications":notifications, "version": version})

def developer(request):
    users = User.objects.all().count()
    all_listings = UserListings.objects.all().count()
    active_listings = UserListings.objects.filter(is_expired = False).count()
    expired_listings = UserListings.objects.filter(is_expired = True).count()
    current_time = timezone.now()
    return render(request, "developer.html", {
        "all_users": users,
        "all_listings":all_listings,
        "active_listings": active_listings,
        "expired_listings": expired_listings,
        "time": current_time
    })

def page_404(request, exception):
    return render(request, "page404.html", status=404)

def sample(request):
    return render(request, "firebase_notifications.html")

def firebase_messaging_sw(request):
    firebase_script = """
    importScripts('https://www.gstatic.com/firebasejs/10.8.1/firebase-app-compat.js');
    importScripts('https://www.gstatic.com/firebasejs/10.8.1/firebase-messaging-compat.js');

    const firebaseConfig = {
        apiKey: "AIzaSyBSCpcctpJNIr26-D73N9-M6Jhxe3pZnk0",
        authDomain: "kku-unofficial-store.firebaseapp.com",
        projectId: "kku-unofficial-store",
        storageBucket: "kku-unofficial-store.appspot.com",
        messagingSenderId: "920854395385",
        appId: "1:920854395385:web:2c52cbe92d41289d912528"
    };

    firebase.initializeApp(firebaseConfig);
    const messaging = firebase.messaging();
    """

    response = HttpResponse(firebase_script, content_type="application/javascript")
    return response

def save_fcm_token(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        token = data.get('token')
        username = request.user.username
        print(token, username)
        fcm_token, created = FCMToken.objects.get_or_create(username=username)
        fcm_token.token = token
        fcm_token.save()
        return JsonResponse({'message': 'Token saved successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

def process_purchase(request):
    # Process purchase logic here

    # Retrieve FCM tokens of users who need to be notified
    tokens = FCMToken.objects.all()

    message_title = "Your notification title"
    message_body = "Your notification message"
    data_message = {
        "body": message_body,
        "title": message_title,
        # You can add more custom data here if needed
    }

    # Send notification to each token
    for token in tokens:
        push_service = FCMNotification(api_key=FCM_Key)
        result = push_service.notify_single_device(registration_id=token.token, data_message=data_message)
        print(result)
    return JsonResponse({'message': 'Purchase processed successfully'})


