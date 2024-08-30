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

def test_read_item(client):
    # Given
    item = Item(name="Test Item", description="This is a test item")
    db.session.add(item)
    db.session.commit()

    # When
    response = client.get(f'/items/{item.id}')

    # Then
    assert response.status_code == 200
    assert b"Test Item" in response.data
    assert b"This is a test item" in response.data
