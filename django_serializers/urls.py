from django.urls import path, include
from rest_framework import routers

# Importando os ViewSets de seus respectivos aplicativos
from products.views import ProductViewSet
from categories.views import CategoryViewSet
from orders.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]