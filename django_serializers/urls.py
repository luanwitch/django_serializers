# projeto/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AlunoViewSet, CursoViewSet
from categories.views import CategoryViewSet
from products.views import ProductViewSet
from orders.views import OrderViewSet

router = DefaultRouter()
# ===========================
# API app
# ===========================
router.register(r'aluno', AlunoViewSet, basename='aluno')
router.register(r'curso', CursoViewSet, basename='curso')

# ===========================
# Categories app
# ===========================
router.register(r'category', CategoryViewSet, basename='category')

# ===========================
# Products app
# ===========================
router.register(r'product', ProductViewSet, basename='product')

# ===========================
# Orders app
# ===========================
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Todas as rotas da API
]
