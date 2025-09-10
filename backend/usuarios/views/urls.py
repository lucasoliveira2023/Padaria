from django.urls import path

from usuarios.views.api_v1 import GetProfileViewUser, LoginView, RegistroUsuarioView

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro-usuario"),
    path("login/", LoginView.as_view(), name="login-usuario"),
    path("profile/", GetProfileViewUser.as_view(), name="user-profile"),
]
