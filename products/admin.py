from django.contrib import admin

# Register your models here.
from products.models import Product, ProductImage
from products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductImageAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
