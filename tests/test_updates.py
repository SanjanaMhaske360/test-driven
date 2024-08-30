from django.test import TestCase
from myapp.models import Product  # Adjust the import according to your project structure

class ProductModelUpdateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a product instance to test updating
        cls.product = Product.objects.create(
            name='Original Product',
            description='Original description.',
            price=1000,  # Example price in cents (e.g., $10.00)
            stock=20
        )

    def test_product_update(self):
        # Update the product's details
        self.product.name = 'Updated Product'
        self.product.description = 'Updated description.'
        self.product.price = 2000  # Updated price in cents (e.g., $20.00)
        self.product.stock = 30
        self.product.save()  # Save the changes to the database

        # Retrieve the updated product from the database
        updated_product = Product.objects.get(id=self.product.id)

        # Check that the updated product’s details match the new values
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.description, 'Updated description.')
        self.assertEqual(updated_product.price, 2000)
        self.assertEqual(updated_product.stock, 30)
