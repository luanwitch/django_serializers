from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import AlunoViewSet, CursoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename='aluno')  # basename singular
router.register(r'cursos', CursoViewSet, basename='curso')

urlpatterns = [
    path('', include(router.urls)),
]
