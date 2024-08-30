import pytest
from myapp import create_app, db
from myapp.models import Item

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_find_by_availability(client):
    # Given
    available_item = Item(name="Available Item", description="This item is available", available=True)
    unavailable_item = Item(name="Unavailable Item", description="This item is not available", available=False)
    db.session.add(available_item)
    db.session.add(unavailable_item)
    db.session.commit()

   
