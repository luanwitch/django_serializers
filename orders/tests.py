from django.test import TestCase
from products.models import Product, Category
from orders.models import Order

class OrderTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Eletrônicos')
        self.product = Product.objects.create(
            name='Smartphone',
            price=500.00,
            stock=10,        
            available=True,  
            category=self.category
        )
        self.order = Order.objects.create(
            product=self.product,
            quantity=1
        )
