from django.contrib import admin
from .models import*

admin.site.register((Maincategory,Subcategory,Brand,Product,testimonial,Buyers,Wishlist,Checkout,CheckoutProducts,contact))


