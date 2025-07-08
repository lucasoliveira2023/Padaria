from django.test import TestCase

from usuarios.models import Usuario
from usuarios.serializers import RegistroUsuarioSerializer


class RegistroUsuarioSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "username": "usuario1",
            "password": "SenhaForte123!",
            "email": "usaurio1@exemple.com",
            "nome_completo": "Usuário Um",
            "cpf": "123.456.789-00",
            "telefone": "11999999999",
            "tipo_usuario": "CLIENTE",
        }
        Usuario.objects.create_user(
            username="existente",
            password="SenhaForte123!",
            email="existente@exemple.com",
            nome_completo="Usuário Existente",
            cpf="111.222.333-04",
        )

    def test_serializer_valido_criacao(self):
        serializer = RegistroUsuarioSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        usuario = serializer.save()
        self.assertEqual(usuario.username, self.valid_data["username"])
        self.assertTrue(usuario.check_password(self.valid_data["password"]))
        self.assertEqual(usuario.cpf, self.valid_data["cpf"])

    def test_serializer_username_duplicado(self):
        data = self.valid_data.copy()
        data["username"] = "existente"
        serializer = RegistroUsuarioSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)
        self.assertEqual(
            serializer.errors["username"][0], "Este nome de usuário já esta em uso."
        )

    def test_serializer_cpf_duplicado(self):
        data = self.valid_data.copy()
        data["cpf"] = "111.222.333-04"
        serializer = RegistroUsuarioSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("cpf", serializer.errors)
        self.assertEqual(serializer.errors["cpf"][0], "Este CPF já está cadastrado.")

    def test_serializer_senha_fraca(self):
        data = self.valid_data.copy()
        data["password"] = "12345678"
        serializer = RegistroUsuarioSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
