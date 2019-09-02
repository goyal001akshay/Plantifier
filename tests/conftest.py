import pytest
from atipcore import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="session")
def resource_uri(app):
    api_prefix = app.config['APPLICATION_ROOT']
    return {
        "calculate-score": f"{api_prefix}/calculate-score"
    }


@pytest.fixture()
def client(app):
    return app.test_client()
