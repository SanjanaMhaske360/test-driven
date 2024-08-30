from django.test import TestCase
from myapp.models import Product  # Adjust the import according to your project structure

class ProductModelListTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create multiple products to test listing
        cls.product1 = Product.objects.create(
            name='Product 1',
            description='Description for product 1.',
            price=1000,  # Example price in cents (e.g., $10.00)
            stock=10
        )
        cls.product2 = Product.objects.create(
            name='Product 2',
            description='Description for product 2.',
            price=2000,  # Example price in cents (e.g., $20.00)
            stock=20
        )
        cls.product3 = Product.objects.create(
            name='Product 3',
            description='Description for product 3.',
            price=3000,  # Example price in cents (e.g., $30.00)
            stock=30
        )

    def test_list_all_products(self):
        # Simulate a GET request to the endpoint that lists all products
        response = self.client.get('/products/')  # Adjust URL according to your routes

        # Ensure the reque
