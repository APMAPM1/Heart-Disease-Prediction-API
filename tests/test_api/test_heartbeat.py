def test_heartbeat(test_client):
    response = test_client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}
