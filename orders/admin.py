from django.contrib import admin

# Register your models here.
from orders.models import Order, ProductInOrder, Status
from products.models import Product


class ProductsInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductsInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = Product


admin.site.register(ProductInOrder, ProductInOrderAdmin)
