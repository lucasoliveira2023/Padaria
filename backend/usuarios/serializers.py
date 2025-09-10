from rest_framework import serializers

from .models import Profile, Usuario


class RegistroUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nome_completo = serializers.CharField()
    cpf = serializers.CharField()
    telefone = serializers.CharField(required=False, allow_blank=True)
    tipo_usuario = serializers.CharField(required=False)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "endereco",
            "data_nascimento",
            "preferencia_horario_atendimento",
            "sexo",
        ]


class UsuarioProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Usuario
        fields = [
            "id",
            "username",
            "email",
            "nome_completo",
            "cpf",
            "telefone",
            "tipo_usuario",
            "profile",
        ]
