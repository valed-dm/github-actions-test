"""client generator for tests"""


from _pytest.fixtures import fixture
from flask.testing import FlaskClient

from app import app


@fixture
def client() -> FlaskClient:
    """client generator"""
    with app.test_client() as test_client:
        yield test_client
