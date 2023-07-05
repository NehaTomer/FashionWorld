
from django.contrib import admin
from django.urls import path
from fashionApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage),
    path('about/',views.aboutpage),
    path('cart/',views.cartpage),
    path('contact/',views.contactpage),
    path('product/<str:mc>/<str:sc>/<str:br>/',views.productpage),
    path('filter/<str:mc>/<str:sc>/<str:br>/<str:filter>/',views.filterpage),
    path('price-filter/<str:mc>/<str:sc>/<str:br>/',views.PriceFilterPage),
    path('search/',views.searchpage),
    path('testimonial/',views.testimonialpage),
    path('product_detail/<int:num>/',views.productdetailpage),
    path('login/',views.loginpage),
    path('signup/',views.signuppage),
    path('forgot-password1/',views.forgotpasswordpage1),
    path('forgot-password2/',views.forgotpasswordpage2),
    path('forgot-password3/',views.forgotpasswordpage3),
    path('addtocart/<int:num>/',views.addtocartpage),
    path('remove-from-cart/<str:num>/',views.removecartpage),
    path('update-cart/<str:num>/<str:op>/',views.updatecartpage),
    path('addtowishlist/<int:num>/',views.wishlistpage),
    path('remove-from-wishlist/<int:num>/',views.removewishlistpage),
    path('place-order/',views.placeorder),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',views.paymentSuccesspage),
    path('re-payment/<str:checkid>/',views.payAgainpage),
    path('confirmation/',views.confirmationpage),
    path('cart/',views.cartpage),
    path('checkout/', views.checkoutpage),
    path('profile/', views.profilepage),
    path('logout/', views.logoutpage),
    path('update-profile/', views.updateprofile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
