from rest_framework import serializers
from .models import Dados, ListaBens, ListaDividas, DadosDividas, DadosBens

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

class DadosDividasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosDividas
        fields = ['id',
                  'empresa',
                  'valor_divida_original',
                  'valor_divida_atual',
                  'tipo_divida',
                  'numero_contrato',
                  'data_divida',
                  'created_date',
                  'updated_date']

class DadosBensSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBens
        fields = ['id',
                  'descricao'
                  'data_aquisicao',
                  'valor_atual',
                  'valor_aquisicao',
                  'tipo',
                  'created_date',
                  'updated_date']
