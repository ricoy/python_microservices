from app.services import HelloWorldService
from app.models import HelloWorldModel


def test_get_hello_world_uppercase():
    model = HelloWorldModel()
    service = HelloWorldService(model)
    assert service.get_hello_world_uppercase() == "HELLO WORLD"
