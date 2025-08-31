from rest_framework import routers
from django.urls import path, include
from .viewsets import CursoViewSet, AlunoViewSet

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'alunos', AlunoViewSet, basename='aluno')

urlpatterns = [
    path('', include(router.urls)),  
]
