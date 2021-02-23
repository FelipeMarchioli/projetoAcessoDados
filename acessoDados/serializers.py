from rest_framework import serializers
from .models import Dados, ListaBens, ListaDividas

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ['id',
                  'cpf',
                  'nome',
                  'endereco',
                  'id_lista_dividas',
                  'idade',
                  'fonte_renda',
                  'id_lista_bens',
                  'created_date',
                  'updated_date']

class DividasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDividas
        fields = ['id',
                  'dividas']

class BensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaBens
        fields = ['id',
                  'bens']
