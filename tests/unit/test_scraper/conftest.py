import pytest


@pytest.fixture
def correct_url() -> str:
    return "https://correcturl.com"


@pytest.fixture
def bad_url() -> str:
    return "htt//badurl.com"
