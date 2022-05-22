from fastapi.testclient import TestClient


def test_endpoint_info(test_client: TestClient):
    # given
    endpoint: str = "/v1/info"
    # when
    response = test_client.get(endpoint)
    # then
    assert response.status_code == 200
    assert response.json() == {"receiver": "Cisco is the best !"}
