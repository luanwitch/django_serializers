from django.urls import path, include
from rest_framework import routers

# Importando os ViewSets de seus respectivos aplicativos
from categories.views import CategoryViewSet
from products.views import ProductViewSet
from orders.views import OrderViewSet

# Criando um roteador para os viewsets
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    # Incluindo as URLs do roteador
    path('', include(router.urls)),
]