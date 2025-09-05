from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category

class CategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Eletrônicos")

    def test_get_categories(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        data = {"name": "Acessórios"}
        response = self.client.post("/api/categories/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
