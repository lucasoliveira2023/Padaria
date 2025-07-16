from rest_framework import serializers


class RegistroUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nome_completo = serializers.CharField()
    cpf = serializers.CharField()
    telefone = serializers.CharField(required=False, allow_blank=True)
    tipo_usuario = serializers.CharField(required=False)
