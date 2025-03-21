import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = FuzzyChoice(["Hat", "Pants", "Shirt", "Apple", "Banana", "Towel"])
    description = factory.Faker("sentence")
    price = FuzzyDecimal(1.0, 500.0, 2)
    available = FuzzyChoice([True, False])
    category = FuzzyChoice([Category.CLOTHS, Category.FOOD, Category.HOUSEWARES])
