from django.urls import path

from acessoDados import views

urlpatterns = [
    path('criar', views.add_dados, name='add_dados'),
    path('buscar/<str:cpf>', views.get_dados, name='get_dados'),
]