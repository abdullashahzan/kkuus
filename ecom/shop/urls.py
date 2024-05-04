from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'shop'
handler404 = 'shop.views.page_404'
handler500 = 'shop.views.page_500'
urlpatterns = [
    path('toggleLanguage/', views.change_language, name='toggleLanguage'),
    path('username_availability/<str:username>', views.check_username_availability, name='username_availability'),
    path('email_availability/<str:email>', views.check_email_availability, name='email_availability'),
    path('developer_dashboard/', views.developer, name='developer'),

    path('', views.index, name="index"),
    path('login/', views.login_user, name="login_user"),
    path('signup/', views.signup_user, name="signup_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('getimage/<str:firebase_path>/', views.get_image, name='get_image'),
    path('home/', views.homepage, name='homepage'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<str:notification_id>', views.delete_notification, name='delete_notification'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('addToWishlist/<str:item_id>', views.add_to_wishlist, name="addToWishlist"),
    path('removeFromWishlist/<str:item_id>', views.remove_from_wishlist, name="removeFromWishlist"),
    path('createNewListing/', views.new_listing, name='new_listing'),

    path('crop-image/', views.crop_image, name='crop_image'), 
    path('createNewPaidListing/<str:invoice>/<str:plan>', views.paid_sale_successful, name='new_paid_listing'),
    
    path('deleteListing/<str:listing_id>', views.delete_listing, name='delete_listing'),
    path('myShop/', views.my_shop, name='my_shop'),
    path('buy/<str:item_id>', views.buy, name='buy'),
    path('purchase/<str:item_id>', views.purchase, name='purchase'),
    path('confirmPurchase/<str:item_id>', views.confirm_purchase, name='confirmPurchase'),
    path('postComment/<str:item_id>', views.comment, name='postComment'),
    path('deleteComment/<str:comment_id>/<str:item_id>', views.delete_comment, name='delete_comment'),
    path('myOrders', views.myOrders, name='myOrders'),
    path('myOrders/accept/<str:item_id>/<str:username>', views.acceptOrder, name='acceptOrder'),
    path('myOrders/reject/<str:item_id>/<str:username>', views.rejectOrder, name='rejectOrder'),
    path('myShop/renew/<str:item_id>', views.renew_item, name='renew_item'),
    path('search/', views.search_item, name='search_item'),
    path('OrderDetails/<str:item_id>', views.order_details, name='order_details'),
    path('profile/', views.profile, name="profile"),
    path('updateAddress/', views.update_address, name='update_address'),
    path('updateInfo/', views.update_info, name='update_info'),
    path('updatePassword/', views.update_password, name='update_password'),
    path('deleteAccount/', views.delete_account, name='delete_account'),

    path('EnableUserNotifications/', views.preEnableNotifications, name='preEnableNotifications'),
    path('enableNotifications/', views.enableNotifications, name='enableNotifications'),
    path('save-fcm-token/', views.save_fcm_token, name='save_fcm_token'),
    path('samplePurchase/', views.process_purchase, name='samplePurchase'),

    path('publishNewNotice/', views.publish_new_notice, name="publish_new_notice"),

]

urlpatterns += staticfiles_urlpatterns()
