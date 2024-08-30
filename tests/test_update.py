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

def test_update_item(client):
    # Given
    item = Item(name="Original Item", description="This is the original item")
    db.session.add(item)
    db.session.commit()
    
    # When
    updated_data = {
        'name': 'Updated Item',
        'description': 'This is the updated item'
    }
    response = client.put(f'/items/{item.id}', json=updated_data)
    
    # Then
    assert response.status_code == 200
    updated_item = Item.query.get(item.id)
    assert updated_item.name == 'Updated Item'
    assert updated_item.description == 'This is the updated item'
