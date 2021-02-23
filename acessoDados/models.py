from django.db import models
from django.utils import timezone

class ListaDividas(models.Model):
  id = models.AutoField(primary_key=True)
  dividas = [models.ForeignObject(to='DadosDividas', on_delete=models.CASCADE, from_fields=['dividas'], to_fields=['id'])]

  def __str__(self):
      return self.id
class DadosDividas(models.Model):  
  empresa = models.CharField(default="", max_length=50)
  valor_divida_original = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  valor_divida_atual = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  tipo_divida = models.CharField(default="", max_length=20)
  numero_contrato = models.IntegerField(default=0)
  data_divida = models.DateField(default=timezone.now)
  created_date = models.DateTimeField(auto_created=True, editable=False, default=timezone.now)
  updated_date = models.DateTimeField(auto_created=True, default=timezone.now)

class ListaBens(models.Model):
  id = models.AutoField(primary_key=True)
  bens = [models.ForeignObject(to='DadosBens', on_delete=models.CASCADE, from_fields=['bens'], to_fields=['id'])]

  def __str__(self):
      return self.id  
      
class DadosBens(models.Model):
  descricao = models.CharField(default="", max_length=50)
  data_aquisicao = models.DateField(default=timezone.now)
  valor_aquisicao = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  valor_atual = models.DecimalField(default=0, max_digits=12, decimal_places=2)
  tipo = models.CharField(default="", max_length=30)
  created_date = models.DateTimeField(auto_created=True, editable=False, default=timezone.now)
  updated_date = models.DateTimeField(auto_created=True, default=timezone.now)

class Dados(models.Model):
  cpf = models.CharField(max_length=11)
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=80)
  id_lista_dividas = models.ForeignKey('ListaDividas', on_delete=models.CASCADE, default=0)
  idade = models.IntegerField(default=0)
  fonte_renda = models.CharField(max_length=50)
  id_lista_bens = models.ForeignKey('ListaBens', on_delete=models.CASCADE, default=0)
  created_date = models.DateTimeField(auto_created=True, editable=False, default=timezone.now)
  updated_date = models.DateTimeField(auto_created=True, default=timezone.now)
  

  def __str__(self):
    return self.cpf
