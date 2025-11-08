from django.db import models
from django.core.validators import MinValueValidator
from .Category import Category
from .Brand import Brand

class Products(models.Model):
    name = models.CharField(max_length=144, null=False, blank=False, db_column='PRODUCTS')
    description = models.TextField(db_column='DESCRIPTION', null=False, blank=False)
    price = models.IntegerField(db_column='PRICE', null=False, blank=False, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.DO_NOTHING, db_column='category_fk')
    brand = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE, db_column='brand_fk')
    color = models.CharField(max_length=144, null=False, blank=False, db_column='COLOR')
    product_image = models.ImageField(upload_to='media/products/', help_text='Upload Images with name as "product_name.jpg" for corrent mapping with Products. Ex. "blue_shirt.jpg".', db_column='PRODUCT_IMAGES')
    is_active = models.BooleanField(db_default=True, db_column='IS_ACTIVE')
    is_deleted = models.BooleanField(db_default=False, db_column='IS_DELETED')
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.name} : {self.description}"