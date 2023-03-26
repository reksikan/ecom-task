from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=32)
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT)

    def __str__(self):
        return self.sku


class Size(models.Model):
    title = models.CharField(max_length=32)
    product = models.ForeignKey(to=Product, related_name='sizes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} of {self.product.sku}'


class Price(models.Model):
    price = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    product_size = models.ForeignKey(to=Size, related_name='prices', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.price} RUB for {self.product_size}'
