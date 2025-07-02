from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from usuarios.serializers import RegistroUsuarioSerializer


class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = RegistroUsuarioSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mesagem": "Usuário registrado com sucesso!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
