import pytest
from app import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = 'Well done! You Successfully deployed your flask app, Now you can start building your app.'
    assert expected_text.encode() in response.data

def test_info(client):
  response = client.get('/info')  
  assert response.status_code == 200 
  expected_text = 'Author: Pandu' 
  assert expected_text.encode() in response.data 