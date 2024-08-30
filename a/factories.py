import factory
from factory import Faker
from myapp.models import Product  # Adjust the import according to your project structure

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker('word')
    description = Faker('sentence')
    price = Faker('random_number', digits=5)
    stock = Faker('random_number', digits=3)

# Optionally, you can define additional methods or override default behavior here.
