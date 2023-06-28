import pytest


@pytest.fixture(scope="module")
def set_group():
    print("start test")
    yield
    print("finish test")
