from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from orders.views import OrderViewSet
from categories.views import CategoryViewSet
from .viewsets import CursoViewSet, AlunoViewSet
from .views import CursoViewSet, AlunoViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'cursos', CursoViewSet, basename="curso")
router.register(r'alunos', AlunoViewSet, basename="aluno")

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
