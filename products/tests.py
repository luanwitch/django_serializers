from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Notebook", price=3500.00)

    def test_get_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        data = {"name": "Mouse Gamer", "price": 150.00}
        response = self.client.post("/api/products/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
