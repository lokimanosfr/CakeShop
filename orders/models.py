from django.db import models
from django.db.models import signals
from landing.models import User
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % (self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    customer_name = models.CharField(
        max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None)
    address = models.ForeignKey(User).name
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status)

    def __str__(self):
        return "%s" % self.customer_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    count_product = models.IntegerField(default=1)
    price_per_item = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)  # Total price *count_product

    def __str__(self):
        return "Имя продукта %s" % (self.product.name)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.count_product * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_postsave(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(
        order=order, is_active=True)
    order_total_price = 0

    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)
    order_total_price = instance.total_price


signals.post_save.connect(product_in_order_postsave, sender=ProductInOrder)
