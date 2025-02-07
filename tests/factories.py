import factory
from your_app.models import Product  # Replace your_app

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('catch_phrase')  # Example: Generates a random catchphrase
    category = factory.Faker('word')      # Example: Generates a random word
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True) # Example: Random price
    available = factory.Faker('boolean')   # Example: Random availability
    # ... other fields
