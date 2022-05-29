from app import app


def test_hello_world_response():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '{"message":"HELLO WORLD"}\n'


def test_not_found_response():
    response = app.test_client().get("/not-found")
    assert response.status_code == 404
