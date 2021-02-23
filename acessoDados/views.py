from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _
from .serializers import DadosSerializer, DividasSerializer, BensSerializer
from .models import Dados, ListaDividas, ListaBens
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from acessoDados.validations import validate_CPF

error_messages = {
    'cpf_exists': _("CPF já existente."),
}

@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_dados(request):
    payload = json.loads(request.body)
    try:
        cpf = validate_CPF(payload["cpf"])

        if Dados.objects.filter(cpf=cpf).exists():
            return JsonResponse({'error': error_messages['cpf_exists']}, safe=False, status=status.HTTP_409_CONFLICT)

        dados = Dados.objects.create(
            nome=payload["nome"],
            endereco=payload["endereco"],
            idade=payload["idade"],
            cpf=cpf,
            fonte_renda=payload["fonte_renda"],
            id_lista_dividas=ListaDividas.objects.create(),
            id_lista_bens=ListaBens.objects.create()
        )
        serializer = DadosSerializer(dados)
        
        return JsonResponse(data={'dados': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except Exception:
        return JsonResponse({'error': 'Ocorreu algum erro no nosso servidor. Tente novamente mais tarde.'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
def get_dados(request, cpf):
    try:
        dados = Dados.objects.filter(cpf=cpf).values()
        serializer = DadosSerializer(list(dados))
        return JsonResponse({'dados': dados}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
