import pytest
from your_app.models import Product
from .factories import ProductFactory

@pytest.mark.django_db
def test_product_read():
    product = ProductFactory()
    retrieved_product = Product.objects.get(pk=product.id)
    assert retrieved_product.name == product.name

# ... similar tests for other functionalities
