from django.urls import path

from usuarios.views import RegistroUsuarioView

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro_usuario"),
]
