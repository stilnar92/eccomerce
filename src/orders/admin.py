from django.contrib import admin

from .models import UserCheckout,UserAddress

admin.site.register(UserCheckout)
admin.site.register(UserAddress)
# Register your models here.
