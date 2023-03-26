from django.contrib import admin

from .models import Product, Brand, Size, Price

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Price)
