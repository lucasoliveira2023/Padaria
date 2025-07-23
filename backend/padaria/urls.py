from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "padaria/usuarios/",
        include(("usuarios.views.urls", "usuarios"), namespace="usuarios"),
    ),
]
