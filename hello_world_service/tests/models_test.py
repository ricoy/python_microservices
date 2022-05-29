from app.models import HelloWorldModel


def test_hello_world_message():
    assert str(HelloWorldModel()) == "Hello World"
