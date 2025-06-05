from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ("ADMIN", "Administrador"),
        ("CLIENTE", "Cliente"),
        ("VENDEDOR", "Vendedor"),
    ]

    nome_completo = models.CharField(
        max_length=150, verbose_name="Nome Completo", db_index=True
    )
    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name="CPF",
        validators=[
            RegexValidator(
                regex=r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
                message="CPF deve estar no formato XXX.XXX.XXX-XX",
            )
        ],
    )
    telefone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Telefone"
    )
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default="CLIENTE",
        db_index=True,
        verbose_name="Tipo de Usuário",
    )
    ativo = models.BooleanField(default=True, db_index=True, verbose_name="Ativo")
    criado_em = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Criado em"
    )
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        indexes = [
            models.Index(fields=["nome_completo"], name="idx_usuario_nome"),
            models.Index(fields=["tipo_usuario"], name="idx_usuario_tipo"),
            models.Index(fields=["ativo"], name="idx_usuario_ativo"),
            models.Index(fields=["criado_em"], name="idx_usuario_criado_em"),
        ]

    def __str__(self):
        return self.username
