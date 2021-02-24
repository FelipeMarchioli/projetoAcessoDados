# Projeto Acesso Dados
Nesse projeto foi elaborada uma ideia inicial de cadastros de vários CPFs afim de consumir uma base de dados para terceiros.

## Stack utilizada
A stack escolhida foi Python com um dos seus frameworks mais conhecidos, o Django.

## Arquitetura Django
Django utiliza o modelo MTV, que consiste na comunicação entre Models, Templates e Views.
Sendo a Model responsável pelo mapeamento do banco de dados, a Template responsável por renderizar as páginas ao usuário, utilizando html, css e até javaScript e a camada Views responsável pelas lógicas de negócio.

Abaixo, pode ser observada a estrutura do projeto:
    projetoAcessoDados
    ├── acessoDados
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── validations.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    ├── projetoAcessoDados
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── .gitignore
    ├── docker-compose.yml
    ├── Dockerfile
    ├── README.md
    ├── requirements.txt

## Acesso APIs
Todas as APIs são fechadas para acesso externo, parceiros que adquirirem o serviço poderá acessar a API com usuário e senha.
Para mais informações sobre as APIs, acesse: [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/447e4540c70259c96e44)