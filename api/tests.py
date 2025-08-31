from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Curso, Aluno

class CursoTests(APITestCase):
    def setUp(self):
        self.curso = Curso.objects.create(codigo_curso="C001", nome_curso="Python", descricao="Curso de Python")

    def test_list_cursos(self):
        url = reverse('curso-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AlunoTests(APITestCase):
    def setUp(self):
        self.curso = Curso.objects.create(codigo_curso="C001", nome_curso="Python", descricao="Curso de Python")
        self.aluno = Aluno.objects.create(nome_aluno="Luan", rg="123456789", cpf="12345678901", data_nascimento="2000-01-01", curso=self.curso)

    def test_list_alunos(self):
        url = reverse('aluno-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
