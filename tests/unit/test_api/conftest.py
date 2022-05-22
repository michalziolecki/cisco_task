from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def test_app() -> FastAPI:
    from src.cisco.api.app import app

    return app


@pytest.fixture
def test_client(test_app: FastAPI) -> TestClient:
    return TestClient(test_app)
