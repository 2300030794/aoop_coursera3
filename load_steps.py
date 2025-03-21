from behave import given
from service.models import db, Product

@given('the following products exist')
def step_impl(context):
    for row in context.table:
        product = Product(
            name=row["name"],
            category=row["category"],
            available=row["available"].lower() == "true"
        )
        db.session.add(product)
    db.session.commit()
