from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from usuarios.models import Usuario


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Usuario.objects.all(),
                message="Este nome de usuário já esta em uso.",
            )
        ]
    )
    cpf = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Usuario.objects.all(), message="Este CPF já está cadastrado."
            )
        ]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Usuario
        fields = [
            "username",
            "password",
            "email",
            "nome_completo",
            "cpf",
            "telefone",
            "tipo_usuario",
        ]

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            nome_completo=validated_data["nome_completo"],
            cpf=validated_data["cpf"],
            telefone=validated_data.get("telefone", ""),
            tipo_usuario=validated_data.get("tipo_usuario", "CLIENTE"),
        )
        return user
