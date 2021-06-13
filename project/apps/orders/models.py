from django.db import models


class Order(models.Model):
    CHOICES = (
        ('New', 'new'),
        ('Accepted', 'accepted'),
        ('Failed', 'failed')
    )
    id = models.AutoField(primary_key = True)
    status = models.CharField(max_length=12,choices=CHOICES, default = 'New')
    created_at = models.DateTimeField()
    external_id = models.CharField(max_length=128,)

    def __str__(self):
        return self.status


class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    id = models.AutoField(primary_key = True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order

