import json

from django.urls import reverse
from django.test import TestCase, Client
from rest_framework import status
from acessoDados.models import Dados, ListaDividas, ListaBens
from acessoDados.serializers import DadosSerializer

client = Client()

class TestPOSTCreateData(TestCase):
  def test_post_create_data_without_cpf(self):
    data = {"nome":"Camila", "endereco":"Rua X, 122", "idade":29, "cpf":"", "fonte_renda":"Desenvolvedora"}

    response = client.post(reverse('add_dados'), data, 'application/json;charset=UTF-8')
    dados = Dados.objects.create(nome=data["nome"],
                                 endereco=data["endereco"],
                                 idade=data["idade"],
                                 cpf=data["cpf"],
                                 fonte_renda=data["fonte_renda"],
                                 id_lista_dividas=ListaDividas.objects.create(),
                                 id_lista_bens=ListaBens.objects.create())
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

  def test_post_create_data_wrong_cpf(self):
    data = {"nome":"Camila", "endereco":"Rua X, 122", "idade":29, "cpf":"40632500830", "fonte_renda":"Desenvolvedora"}

    response = client.post(reverse('add_dados'), data, 'application/json;charset=UTF-8')
    dados = Dados.objects.create(nome=data["nome"],
                                 endereco=data["endereco"],
                                 idade=data["idade"],
                                 cpf=data["cpf"],
                                 fonte_renda=data["fonte_renda"],
                                 id_lista_dividas=ListaDividas.objects.create(),
                                 id_lista_bens=ListaBens.objects.create())
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

  def test_post_create_data(self):
    data = {"nome":"Camila", "endereco":"Rua X, 122", "idade":29, "cpf":"40632500832", "fonte_renda":"Desenvolvedora"}

    response = client.post(reverse('add_dados'), data, 'application/json;charset=UTF-8')
    dados = Dados.objects.create(nome=data["nome"],
                                 endereco=data["endereco"],
                                 idade=data["idade"],
                                 cpf=data["cpf"],
                                 fonte_renda=data["fonte_renda"],
                                 id_lista_dividas=ListaDividas.objects.create(),
                                 id_lista_bens=ListaBens.objects.create())
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)