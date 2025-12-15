import pytest

@pytest.fixture
def set_up():
    print("Browser Setup")
    yield
    print("Browser Teardown")
