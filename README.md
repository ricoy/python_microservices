# POC de microserviços com Flask

## Testando o microserviço hello_world_service
- Instalar o [Pyenv](https://github.com/pyenv/pyenv)
- Instalar a versão `3.10` do Python com o Pyenv
```bash
pyenv install 3.10.0
```
- Entrar no diretório `python_microservices/hello_world_service` e definir a versão local do Python
```bash
pyenv local 3.10.0
```
- Instalar o pipenv
```bash
pip install pipenv
```
- Instalar as dependências do projeto
```bash
pipenv install
```
- Inicializar o serviço
```bash
pipenv run dev
```
- Acesse o serviço em [localhost:5000](http://localhost:5000)
  
## Executando o serviço com Docker
- Realizar o build da imagem a partir do Dockerfile existente
```bash
docker build -t hello_world_service .
```
- Criar o container do serviço
```bash
docker run -p 5000:5000 -d hello_world_service
```
- Acesse o serviço em [localhost:5000](http://localhost:5000)