"""This test the homepage"""

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Chia-Lin's HomePage" in response.data
