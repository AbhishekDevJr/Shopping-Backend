from django.db import models
from users.models.CustomUser import CustomUser
from .Products import Products

class Cart:
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, related_name='cart_products')
    cart_quantity = models.IntegerField(db_default=0, db_column='CART_QUANTITY')
    cart_value = models.DecimalField(db_default=0.00, db_column='CART_VALUE')
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.user.username} : {self.cart_quantity} - {self.cart_value}"
    