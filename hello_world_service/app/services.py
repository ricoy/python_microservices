# camada de implementacao das regras de negocio e validacoes dos servicos
from .models import HelloWorldModel


class HelloWorldService:
    def __init__(self, model: HelloWorldModel):
        self.model = model

    def get_hello_world_uppercase(self) -> str:
        return str.upper(str(self.model))
