from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Curso, Aluno

class CursoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.curso = Curso.objects.create(
            codigo_curso="C001",
            nome_curso="Python Básico",
            descricao="Curso introdutório"
        )

    def test_list_cursos(self):
        url = reverse('curso-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_curso(self):
        url = reverse('curso-list')
        data = {
            "codigo_curso": "C002",
            "nome_curso": "Django",
            "descricao": "Curso avançado"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AlunoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.curso = Curso.objects.create(
            codigo_curso="C001",
            nome_curso="Python Básico",
            descricao="Curso introdutório"
        )
        self.aluno = Aluno.objects.create(
            nome_aluno="Luan",
            email="luan@example.com",
            rg="123456789",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            curso=self.curso
        )

    def test_list_alunos(self):
        url = reverse('aluno-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_aluno(self):
        url = reverse('aluno-list')
        data = {
            "nome_aluno": "Maria",
            "email": "maria@example.com",
            "rg": "987654321",
            "cpf": "10987654321",
            "data_nascimento": "1999-05-10",
            "curso": self.curso.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
