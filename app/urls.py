from django.urls import path
from .views import *
from django.contrib import admin
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('livros/', LivrosView.as_view(), name='livros'),
    path('reserva/', EmprestimoView.as_view(),
    name='reserva'),
    path('cidade/', CidadesView.as_view(),
    name='cidade'),
    path('autor/', AutoresView.as_view(), name='autor'),
    path('editor/', EditorasView.as_view(),
    name='editora'),
    path('genero/', GenerosView.as_view(),
    name='genero'),
    path('usuario/', UsuariosView.as_view(),
    name='usuario'),
]