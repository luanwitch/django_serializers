from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet
from products.views import ProductViewSet
from orders.views import OrderViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]
