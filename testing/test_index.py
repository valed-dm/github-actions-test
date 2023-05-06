"""views tests"""


def test_index(client):
    """testing index view"""
    response = client.get("/")
    assert response.status_code == 200
