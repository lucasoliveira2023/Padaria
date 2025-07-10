from django.urls import reverse
from rest_framework.test import APITestCase

from usuarios.models import Usuario


class RegistroUsuarioViewTest(APITestCase):
    def setUp(self):
        self.url = reverse(
            "usuarios:registro-usuario"
        )  # Ajuste para o nome correto da url

    def test_cadastro_usuario_com_sucesso(self):
        dados = {
            "username": "lucas123",
            "email": "lucas@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Silva",
            "cpf": "12345678901",
            "telefone": "11999999999",
            "tipo_usuario": "CLIENTE",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 201)
        # self.assertIn("messagem", response.data)
        self.assertTrue(Usuario.objects.filter(username="lucas123").exists())

    def test_falha_cpf_duplicado(self):
        Usuario.objects.create_user(
            username="outrousuario",
            email="outro@example.com",
            password="SenhaFort3#",
            nome_completo="Outro Usuário",
            cpf="12345678901",
            telefone="11988888888",
            tipo_usuario="CLIENTE",
        )
        dados = {
            "username": "novo_usuario",
            "email": "novo@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Novo Usuário",
            "cpf": "12345678901",  # cpf duplicado
            "telefone": "11977777777",
            "tipo_usuario": "CLIENTE",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("cpf", response.data)

    def test_falha_username_duplicado(self):
        Usuario.objects.create_user(
            username="lucas123",
            email="lucas@example.com",
            password="SenhaFort3#",
            nome_completo="Lucas Silva",
            cpf="09876543210",
            telefone="11999999999",
            tipo_usuario="CLIENTE",
        )
        dados = {
            "username": "lucas123",  # username duplicado
            "email": "novo@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Novo Usuário",
            "cpf": "11122233344",
            "telefone": "11977777777",
            "tipo_usuario": "CLIENTE",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("username", response.data)

    def test_falha_cpf_formato_invalido(self):
        dados = {
            "username": "usuario2",
            "email": "usuario2@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Usuário Teste",
            "cpf": "1234abcd567",  # inválido (não numérico)
            "telefone": "11999999999",
            "tipo_usuario": "CLIENTE",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("cpf", response.data)

    def test_falha_serializer_invalido(self):
        dados = {
            "username": "",
            "email": "email-invalido",
            "password": "",
            "nome_completo": "",
            "cpf": "",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("username", response.data)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)
        self.assertIn("cpf", response.data)
        self.assertIn("nome_completo", response.data)
