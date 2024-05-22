from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'shop'

handler404 = 'shop.views.page_404'
handler500 = 'shop.views.page_500'

urlpatterns = [
    # Index link
    path('', views.index, name="index"),

    # Misc. links
    path('toggleLanguage/', views.change_language, name='toggleLanguage'),
    path('getimage/<str:firebase_path>/', views.get_image, name='get_image'),
    path('crop-image/', views.crop_image, name='crop_image'), 
    path('username_availability/<str:username>', views.check_username_availability, name='username_availability'),
    path('email_availability/<str:email>', views.check_email_availability, name='email_availability'),

    # User authentication links
    path('login/', views.login_user, name="login_user"),
    path('signup/', views.signup_user, name="signup_user"),
    path('logout/', views.logout_user, name="logout_user"),

    # Notification links
    path('notifications/<str:notification_id>/', views.delete_notification, name='delete_notification'),
    path('DeleteAll/', views.delete_all_notification, name='delete_all_notifications'),

    # Wishlist links
    path('addToWishlist/<str:item_id>', views.add_to_wishlist, name="addToWishlist"),
    path('removeFromWishlist/<str:item_id>', views.remove_from_wishlist, name="removeFromWishlist"),

    # Working with listing links
    path('createNewListing/', views.new_listing, name='new_listing'),
    path('createNewPaidListing/<str:invoice>/', views.paid_sale_successful, name='new_paid_listing'),
    path('deleteListing/<str:listing_id>', views.delete_listing, name='delete_listing'),
    path('myShop/renew/', views.renew_item, name='renew_item'),
    path('hideListing/<str:item_id>/', views.hide_listing, name='hide_listing'),
    path('showListing/<str:item_id>/', views.show_listing, name='show_listing'),

    # Purchase links
    path('purchase/', views.purchase, name='purchase'),
    path('confirmPurchase/<str:item_id>', views.confirm_purchase, name='confirmPurchase'),

    # Links for comments
    path('postComment/<str:item_id>', views.comment, name='postComment'),
    path('deleteComment/<str:comment_id>/<str:item_id>', views.delete_comment, name='delete_comment'),
    
    # Seller order page links
    path('myOrders/accept/<str:item_id>/<str:username>', views.acceptOrder, name='acceptOrder'),
    path('myOrders/reject/<str:item_id>/<str:username>', views.rejectOrder, name='rejectOrder'),

    # Profile settings links
    path('updateAddress/', views.update_address, name='update_address'),
    path('updateInfo/', views.update_info, name='update_info'),
    path('updatePassword/', views.update_password, name='update_password'),
    path('deleteAccount/', views.delete_account, name='delete_account'),

    # Website pages
    path('home/', views.homepage, name='homepage'),
    path('notifications/', views.notifications, name='notifications'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('myShop/', views.my_shop, name='my_shop'),
    path('buy/<str:item_id>', views.buy, name='buy'),
    path('myOrders', views.myOrders, name='myOrders'),
    path('OrderDetails/<str:item_id>', views.order_details, name='order_details'),
    path('search/', views.search_item, name='search_item'),
    path('profile/', views.profile, name="profile"),

    # Developer dashboard links
    path('developer_dashboard/', views.developer, name='developer'),
    path('add_to_developers_pick/<str:item_id>/', views.add_to_developers_pick, name='add_to_developers_pick'),
    path('remove_from_developers_pick/<str:item_id>/', views.remove_from_developers_pick, name='remove_from_developers_pick'),
    path('publishNewNotice/', views.publish_new_notice, name="publish_new_notice"),

    # Push notification links
    path('EnableUserNotifications/', views.preEnableNotifications, name='preEnableNotifications'),
    path('enableNotifications/', views.enableNotifications, name='enableNotifications'),
    path('save-fcm-token/', views.save_fcm_token, name='save_fcm_token'),
    path('samplePurchase/', views.process_purchase, name='samplePurchase'),

    # Terms and Conditions link
    path('TermsAndConditions/', views.terms_conditions, name="terms_conditions"),

]

urlpatterns += staticfiles_urlpatterns()
