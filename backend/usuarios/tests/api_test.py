from rest_framework import status
from rest_framework.test import APITestCase

from usuarios.models import Usuario


class RegistroUsuarioViewTest(APITestCase):
    def setUp(self):
        self.url = "/padaria/usuarios/registro/"
        self.valid_payload = {
            "username": "lucasdev",
            "password": "SenhaForte2025!",
            "nome_completo": "Lucas Oliveira",
            "email": "lucas@exemplo.com",
            "cpf": "123.456.789-00",
        }

    def test_criacao_usuario_com_dados_validos(self):
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["mensagem"], "Usuário registrado com sucesso!")
        self.assertTrue(Usuario.objects.filter(username="lucasdev").exists())

    def test_rejeita_usuario_sem_nome_completo(self):
        payload = self.valid_payload.copy()
        del payload["nome_completo"]
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nome_completo", response.data)

    def test_rejeitar_usuario_com_cpf_duplicado(self):
        Usuario.objects.create_user(
            username="outro_user",
            password="SenhaForte2025!",
            nome_completo="Outro Nome",
            cpf="123.456.789-00",
        )
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("cpf", response.data)

    def test_rejeita_usuario_com_nome_duplicado(self):
        Usuario.objects.create_user(
            username="lucasdev",
            password="SenhaForte2025!",
            nome_completo="Outro Nome",
            cpf="999.999.999-99",
        )
        response = self.client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)

    def test_rejeita_senha_fraca(self):
        payload = self.valid_payload.copy()
        payload["password"] = "12345678"
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_rejeita_usuario_com_cpf_invalido(self):
        payload = self.valid_payload.copy()
        payload["cpf"] = "12345678900"
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("cpf", response.data)
