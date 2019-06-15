
import pytest
from fixture.application import Application

# initialize fixture
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
