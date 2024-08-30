from django.test import TestCase
from myapp.models import Product  # Adjust the import according to your project structure

class ProductModelFindByNameTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create multiple products to test finding by name
        cls.product1 = Product.objects.create(
            name='Product A',
            description='Description for product A.',
            price=1000,  # Example price in cents (e.g., $10.00)
            stock=10
        )
        cls.product2 = Product.objects.create(
            name='Product B',
            description='Description for product B.',
            price=2000,  # Example price in cents (e.g., $20.00)
            stock=20
  
