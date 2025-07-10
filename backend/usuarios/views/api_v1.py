# 'view usuario'
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from usuarios.models import Usuario
from usuarios.serializers import RegistroUsuarioSerializer


class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        if Usuario.objects.filter(cpf=data["cpf"]).exists():
            return Response(
                {"cpf": ["Este CPF já está cadastrado"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Usuario.objects.filter(username=data["username"]).exists():
            return Response(
                {"username": ["Este nome de usuário já está em uso."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not data["cpf"].isdigit() or len(data["cpf"]) != 11:
            return Response(
                {"cpf": ["CPF inválido. Deve conter 11 dígitos numéricos."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Usuario.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            nome_completo=data["nome_completo"],
            cpf=data["cpf"],
            telefone=data.get("telefone", ""),
            tipo_usuario=data.get("tipo_usuario", "CLIENTE"),
        )

        return Response(
            {"messagem": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED
        )
