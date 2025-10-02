from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from orders.models import Order
from products.models import Product
from categories.models import Category

class OrderTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Eletrônicos')
        self.product = Product.objects.create(name='Smartphone', price=1000.00, category=self.category)

    def test_create_order(self):
        url = reverse('order-list')  
        data = {'product_id': self.product.id, 'quantity': 2, 'status': 'pending'}  # usar product_id
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_orders(self):
        order = Order.objects.create(product=self.product, quantity=2, status='pending')
        url = reverse('order-detail', args=[order.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
