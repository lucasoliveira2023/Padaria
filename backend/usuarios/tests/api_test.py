from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

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

    def test_cpf_com_letras_retorna_erro(self):
        dados = {
            "username": "usercpf",
            "email": "usercpf@example.com",
            "password": "SenhaForte3#",
            "nome_completo": "Usuario CPF Inválido",
            "cpf": "abc12345678",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("cpf", response.data)

    def test_cpf_com_tamanho_incorreto(self):
        dados = {
            "username": "usercpf2",
            "email": "usercpf2@exemple.com",
            "password": "SenhaFor3#",
            "nome_completo": "Usuário CPF Curto",
            "cpf": "12345678",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("cpf", response.data)

    def test_usuario_criado_sucesso(self):
        dados = {
            "username": "lucasview",
            "email": "lucasview@example.com",
            "password": "SenhaFort3#",
            "nome_completo": "Lucas Teste",
            "cpf": "98765432100",
            "telefone": "11999999999",
            "tipo_usuario": "CLIENTE",
        }
        response = self.client.post(self.url, data=dados, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Usuario.objects.filter(username="lucasview").exists())


class LoginViewTest(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = Usuario.objects.create_user(
            username=self.username,
            password=self.password,
            email="login@exemple.com",
            nome_completo="Login Test",
            cpf="12345678900",
        )
        self.url = reverse("usuarios:login-usuario")

    def test_login_sucesso(self):
        dados = {"username": self.username, "password": self.password}
        response = self.client.post(self.url, data=dados, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["username"], self.username)

    def test_login_credenciais_invalidas(self):
        dados = {"username": self.username, "password": "senhaerrada"}
        response = self.client.post(self.url, data=dados, format="json")

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["detail"], "Usuário ou senha inválidos.")


class GetProfileViewUserTests(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = Usuario.objects.create_user(
            username=self.username,
            password=self.password,
            email="test@exemple.com",
            nome_completo="Test User",
            cpf="12345678901",
        )

        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)
        self.url = reverse("usuarios:user-profile")

    def test_get_profile_autenticado(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.get(self.url, format="json")

        self.assertEqual(response.data["username"], self.username)
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["cpf"], self.user.cpf)
        self.assertEqual(response.data["nome_completo"], self.user.nome_completo)
        self.assertEqual(response.data["tipo_usuario"], self.user.tipo_usuario)

        self.assertIn("sexo", response.data["profile"])
        self.assertIn("endereco", response.data["profile"])
        self.assertIn("data_nascimento", response.data["profile"])

    def test_get_profile_nao_autenticado(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
