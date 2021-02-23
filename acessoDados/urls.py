from django.urls import path

from acessoDados import views

urlpatterns = [
    path('criar', views.add_dados, name='add_dados'),
    path('buscar/<str:cpf>', views.get_dados_gerais, name='get_dados_gerais'),
    path('buscar/dividas/<str:cpf>', views.get_dados_dividas, name='get_dados_dividas'),
    path('buscar/bens/<str:cpf>', views.get_dados_bens, name='get_dados_bens'),
]