from django.db import models
from shopping_data.models.Cart import Cart
from shopping_data.models.Products import Products

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', db_column='CART_ID')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_products', db_column='PRODUCT_ID')
    product_quantity = models.IntegerField(default=0, db_default=0, db_column='PRODUCT_QUANTITY')
    total_value = models.DecimalField(default=0.0, db_default=0.0, db_column='TOTAL_VALUE', max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
       return f"Cart ID - {self.cart.pk} || Product ID - {self.product.pk}"