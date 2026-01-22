from django.db import models
from users.models.CustomUser import CustomUser
from .Products import Products

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField(db_default=0, db_column='CART_QUANTITY')
    cart_value = models.DecimalField(db_default=0.00, db_column='CART_VALUE', max_digits=10, decimal_places=2)
    is_cart_active = models.BooleanField(db_default=False, db_column='IS_CART_ACTIVE')
    created_date = models.DateField(auto_now_add=True, db_column='CREATED_DATE')
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.user.username} : {self.cart_quantity} - {self.cart_value}"
    