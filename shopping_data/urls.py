from django.urls import path
from .views import BrandView, CategoryView, ProductView

urlpatterns = [
    path('brand-list', BrandView.as_view(), name="brand-list"),
    path('brand-list/<str:brand_id>', BrandView.as_view(), name="brand-list-detail"),
    path('category-list', CategoryView.as_view(), name="category-list"),
    path('category-list/<str:category_id>', CategoryView.as_view(), name="category-detail"),
    path('product-list', ProductView.as_view(), name="product-list"),
    path('paroduct-list/<str:product_id>', ProductView.as_view(), name="product-detail")
]