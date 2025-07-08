from django.core.exceptions import ValidationError
from django.test import TestCase

from usuarios.models import Usuario


class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username="lucastest",
            password="SenhaForte2025!",
            nome_completo="Lucas Teste",
            cpf="123.456.789-00",
            email="lucas@exemple.com",
        )

    def test_str_retorn_username(self):
        self.assertEqual(str(self.usuario), "lucastest")

    def test_tipo_usuario_padrao_cleinte(self):
        self.assertEqual(self.usuario.tipo_usuario, "CLIENTE")

    def test_ativo_padrao_true(self):
        self.assertTrue(self.usuario.ativo)

    def test_criacao_usuario_com_mesmo_cpf_falha(self):
        with self.assertRaises(Exception):
            Usuario.objects.create_user(
                username="outrouser",
                password="SenhaForte2025!",
                nome_completo="Outro Nome",
                cpf="123.456.789-00",
                email="outro@exemple.com",
            )

    def test_validacao_cpf_invalido(self):
        usuario = Usuario(
            username="usuario2",
            nome_completo="Teste CPF",
            cpf="12345678900",
            email="cpf@invalido.com",
        )
        with self.assertRaises(ValidationError):
            usuario.full_clean()

    def test_str_method(self):
        usuario = Usuario.objects.create_user(
            username="testuser",
            password="SenhaForte2025!",
            nome_completo="Test User",
            cpf="123.456.789-10",
            email="testuser@example.com",
        )
        self.assertEqual(str(usuario), "testuser")
