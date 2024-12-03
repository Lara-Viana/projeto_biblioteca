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
<<<<<<< HEAD
    path('genero/', GenerosView.as_view(),
    name='genero'),
    path('usuario/', UsuariosView.as_view(),
    name='usuario'),
=======
    path('leitor/', LeitoresView.as_view(),
    name='leitor'),
    path('genero/', GenerosView.as_view(),
    name='genero'),
>>>>>>> a1dde5cf14dbdebde22c51279d35322aab0d0d46
]