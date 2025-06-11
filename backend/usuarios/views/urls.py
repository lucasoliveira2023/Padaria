from django.urls import path

from .api_v1 import LoginView

urlpatterns = [
    path("usuarios/login/", LoginView.as_view(), name="login"),
]
