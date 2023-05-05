from app import app
from _pytest.fixtures import fixture
from flask.testing import FlaskClient


@fixture
def client() -> FlaskClient:
    with app.test_client() as test_client:
        yield test_client
