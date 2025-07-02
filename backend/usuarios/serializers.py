from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from usuarios.models import Usuario


class RegistroUsuarioSerializer(serializers.ModelSerializer):
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

    def validate_username(self, value):
        if Usuario.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nome de usuário já esta em uso.")
        return value

    def validate_cpf(self, value):
        if Usuario.objects.filter(cpf=value).exists():
            raise serializers.ValidationError("Este CPF já está cadastrado.")
        return value

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
