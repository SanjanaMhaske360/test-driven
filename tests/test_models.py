from django.test import TestCase
from myapp.models import Product  # Adjust the import according to your project structure

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a single product to test reading
        cls.product = Product.objects.create(
            name='Sample Product',
            description='This is a sample product description.',
            price=1999,  # Example price in cents (e.g., $19.99)
            stock=50
        )

    def test_product_read(self):
        # Retrieve the product from the database
        product = Product.objects.get(id=self.product.id)
        
        # Check that the retrieved product matches the expected values
        self.assertEqual(product.name, 'Sample Product')
        self.assertEqual(product.description, 'This is a sample product description.')
        self.assertEqual(product.price, 1999)
        self.assertEqual(product.stock, 50)
