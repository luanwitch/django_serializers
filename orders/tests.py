from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order

class OrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.order = Order.objects.create(
            product="Notebook",
            quantity=2,
            status="pending"
        )

    def test_get_orders(self):
        response = self.client.get("/api/orders/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        data = {
            "product": "Mouse",
            "quantity": 1,
            "status": "completed"
        }
        response = self.client.post("/api/orders/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
