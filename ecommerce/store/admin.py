from django.contrib import admin
from . models import *
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'image',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
