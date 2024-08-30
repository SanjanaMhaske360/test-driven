from django.test import TestCase
from myapp.models import Product  # Adjust the import according to your project structure

class ProductModelDeleteTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a product instance to test deleting
        cls.product = Product.objects.create(
            name='Product to Delete',
            description='This product will be deleted.',
            price=5000,  # Example price in cents (e.g., $50.00)
            stock=10
        )

    def test_product_delete(self):
        # Check that the product exists before deleting
        self.assertTrue(Product.objects.filter(id=self.product.id).exists())
        
        # Delete the product
        self.product.delete()
        
        # Check that the product no longer exists
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
