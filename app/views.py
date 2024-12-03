from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
#from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

#class IndexView(View):
#def get(self, request, *args, **kwargs):
#return render(request, 'index.html')

class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})
# def post(self, request, *args, **kwargs):
class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        emprestimos = Emprestimo.objects.all()
        return render(request, 'emprestimo.html',
{'emprestimos': emprestimos})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
    
class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})
    
class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})
    
class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html',
{'leitores': leitores})
    
class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})
    
class UFsView(View):
    def get(self, request, *args, **kwargs):
        ufs = UF.objects.all()
        return render(request, 'uf.html', {'ufs': ufs})
    
class UsuariosView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})