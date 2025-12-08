from django.urls import path
from .views import BrandView, CategoryView

urlpatterns = [
    path('brand-list', BrandView.as_view(), name="brand-list"),
    path('brand-list/<str:brand_id>', BrandView.as_view(), name="brand-list-detail"),
    path('category-list', CategoryView.as_view(), name="category-list"),
    path('category-list/<str:category_id>', CategoryView.as_view(), name="category-detail")
]