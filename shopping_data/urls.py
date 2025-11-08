from django.urls import path
from .views import BrandView

urlpatterns = [
    path('brand-list', BrandView.as_view(), name="brand-list"),
    path('brand-list/<str:brand_id>', BrandView.as_view(), name="brand-list-detail")
]