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
    Color = models.CharField(max_length=144, null=False, blank=False, db_column='COLOR')
    ProductImage = models.FileField()
    