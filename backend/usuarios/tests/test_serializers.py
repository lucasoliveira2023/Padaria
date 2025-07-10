from rest_framework.test import APITestCase

from usuarios.serializers import RegistroUsuarioSerializer


class RegistroUsuarioSerializerTest(APITestCase):
    def test_serializer_valido(self):
        dados = {
            "username": "lucas123",
            "email": "lucas@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Silva",
            "cpf": "12345678901",
            "telefone": "11999999999",
            "tipo_usuario": "CLIENTE",
        }
        serializer = RegistroUsuarioSerializer(data=dados)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["username"], "lucas123")

    def test_serializer_falha_email_invalido(self):
        dados = {
            "username": "lucas123",
            "email": "email-invalido",
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Silva",
            "cpf": "12345678901",
            "telefone": "11999999999",
        }
        serializer = RegistroUsuarioSerializer(data=dados)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_serializer_falha_campo_obrigatorio_faltando(self):
        dados = {
            "username": "lucas123",
            # email faltando
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Silva",
            "cpf": "12345678901",
        }
        serializer = RegistroUsuarioSerializer(data=dados)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_serializer_telefone_opcional(self):
        dados = {
            "username": "lucas123",
            "email": "lucas@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Silva",
            "cpf": "12345678901",
            # telefone ausente
        }
        serializer = RegistroUsuarioSerializer(data=dados)
        self.assertTrue(serializer.is_valid())

    def test_serializer_tipo_usuario_opcional(self):
        dados = {
            "username": "lucas123",
            "email": "lucas@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Silva",
            "cpf": "12345678901",
            "telefone": "11999999999",
            # tipo_usuario ausente
        }
        serializer = RegistroUsuarioSerializer(data=dados)
        self.assertTrue(serializer.is_valid())
