from django.contrib import admin


from app.models import (
    Product,
    Order
)


admin.site.register(Product)
admin.site.register(Order)