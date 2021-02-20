import datetime

from .validations import validate_CPF
from django.db import models

class ListaDividas(models.Model):
  id = models.AutoField(primary_key=True)
  empresa = models.CharField(default="", max_length=50)
  valor_divida_original = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  valor_divida_atual = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  tipo_divida = models.CharField(default="", max_length=20)
  numero_contrato = models.IntegerField(default=0)
  data_divida = models.DateField(default=datetime.date.today)

class ListaBens(models.Model):
  id = models.AutoField(primary_key=True)
  descricao = models.CharField(default="", max_length=50)
  valor_aquisicao = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  valor_atual = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  tipo = models.CharField(default="", max_length=30)

class Dados(models.Model):
  cpf = models.CharField(max_length=11, validators=[validate_CPF])
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=80)
  id_lista_dividas = models.ForeignKey('ListaDividas', on_delete=models.CASCADE)
  idade = models.IntegerField(default=0)
  fonte_renda = models.CharField(max_length=50)
  lista_bens = models.ForeignKey('ListaBens', on_delete=models.CASCADE)
