from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from categories.models import Category

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
