from django.test import TestCase
from myapp.models import Product, Category  # Adjust the import according to your project structure

class ProductModelFindByCategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create some categories
        cls.category1 = Category.objects.create(name='Electronics')
        cls.category2 = Category.objects.create(name='Books')

        # Create products for each category
        cls.product1 = Product.objects.create(
            name='Laptop',
            description='A high-performance laptop.',
            price=100000,  # Example price in cents (e.g., $1000.00)
            stock=5,
            category=cls.category1
        )
        cls.product2 = Product.objects.create(
            name='Smartphone',
            description='A latest model smartphone.',
            price=60000,  # Example price in cents (e.g., $600.00)
 
