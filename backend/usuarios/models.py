from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def __str__(self):  # pragma: no cover
        return self.username


class Profile(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
    ]

    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name="profile"
    )
    endereco = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Endereço"
    )
    data_nascimento = models.DateField(
        blank=True, null=True, verbose_name="Data de Nascimento"
    )
    preferencia_horario_atendimento = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Horario de Atendimento Preferido",
    )
    sexo = models.CharField(
        max_length=1, choices=SEXO_CHOICES, default="O", verbose_name="sexo"
    )

    def __str__(self):
        return f"Profile de {self.usuario.username}"


@receiver(post_save, sender=Usuario)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usuario=instance)


@receiver(post_save, sender=Usuario)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()
