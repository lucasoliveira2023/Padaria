from django.urls import path

from usuarios.views.api_v1 import RegistroUsuarioView

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro-usuario"),
]
