from django.contrib import admin
from .models import Offer, Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(Offer, OffersAdmin)
