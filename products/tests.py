from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product
from categories.models import Category

class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Eletrônicos')

    def test_create_product(self):
        url = reverse('product-list')  # corrigido
        data = {'name': 'Smartphone', 'price': 1000.00, 'category_id': self.category.id}  
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_products(self):
        product = Product.objects.create(name='Smartphone', price=1000.00, category=self.category)
        url = reverse('product-detail', args=[product.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


