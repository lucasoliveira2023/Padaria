from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response(
                {
                    "refresh": refresh_token,
                    "access": access_token,
                    "username": user.username,
                }
            )
        else:
            return Response(
                {"detail": "Usuário ou senha inválidos."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
