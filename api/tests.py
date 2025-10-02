from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Aluno, Curso
from products.models import Product
from categories.models import Category
from orders.models import Order

# ===========================
# Testes de Aluno
# ===========================
class AlunoTests(APITestCase):
    def setUp(self):
        # Criando um curso para o aluno (obrigatório)
        self.curso = Curso.objects.create(
            codigo_curso='C001',
            nome_curso='Python Básico',
            descricao='Curso de Python básico'
        )

    def test_create_aluno(self):
        url = reverse('aluno-list')  # nome do router
        data = {
            'nome_aluno': 'Luan',
            'rg': '123456789',
            'cpf': '12345678901',
            'data_nascimento': '2000-01-01',
            'curso': self.curso.id,
            'email': 'luan@email.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_alunos(self):
        Aluno.objects.create(
            nome_aluno='Luan',
            rg='123456788',
            cpf='12345678902',
            data_nascimento='2000-01-01',
            curso=self.curso,
            email='luan2@email.com'
        )
        url = reverse('aluno-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# ===========================
# Testes de Curso
# ===========================
class CursoTests(APITestCase):
    def test_create_curso(self):
        url = reverse('curso-list')
        data = {
            'codigo_curso': 'C002',
            'nome_curso': 'Django Avançado',
            'descricao': 'Curso avançado de Django'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_cursos(self):
        Curso.objects.create(
            codigo_curso='C003',
            nome_curso='JavaScript Básico',
            descricao='Curso de JS básico'
        )
        url = reverse('curso-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# ===========================
# Testes de Category
# ===========================
class CategoryTests(APITestCase):
    def test_create_category(self):
        url = reverse('category-list')
        data = {'name': 'Eletrônicos'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        Category.objects.create(name='Eletrônicos')
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# ===========================
# Testes de Product
# ===========================
class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Eletrônicos')

    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'Smartphone', 'price': 1000.00, 'category_id': self.category.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_products(self):
        product = Product.objects.create(name='Smartphone', price=1000.00, category=self.category)
        url = reverse('product-detail', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# ===========================
# Testes de Order
# ===========================
class OrderTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Eletrônicos')
        self.product = Product.objects.create(name='Smartphone', price=1000.00, category=self.category)

    def test_create_order(self):
        url = reverse('order-list')
        data = {'product_id': self.product.id, 'quantity': 2, 'status': 'pending'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_orders(self):
        order = Order.objects.create(product=self.product, quantity=2, status='pending')
        url = reverse('order-detail', args=[order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
