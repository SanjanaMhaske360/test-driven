from behave import given
from myapp import db
from myapp.models import Product

@given('the following products:')
def step_impl(context):
    # Clear existing data
    db.session.query(Product).delete()
    db.session.commit()
    
    # Load products from the table in the feature file
    for row in context.table:
        product = Product(
            name=row['name'],
            description=row['description'],
            price=float(row['price']),
            available=row['available'] == 'True'
        )
        db.session.add(product)
    db.session.commit()
