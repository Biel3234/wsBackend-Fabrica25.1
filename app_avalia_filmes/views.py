from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import *

from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View, TemplateView

import requests


def usuario_sucesso(request):
    return render(request, 'sucesso_cria_usuario.html')

def deletar_sucesso(request):
    return render(request, 'sucesso_deleta_usuario.html')

def buscador(titulo):
    url = f"http://www.omdbapi.com/?apikey=89efe44c&t={titulo}"
    buscar = requests.get(url)
    dados = buscar.json()

    if dados.get('Response') == 'True':
        return {
            "titulo": dados.get("Title"),
            "genero": dados.get("Genre"),
            "ano": dados.get("Year"),
        }


class Home(TemplateView):
    template_name='home.html'
        
# CRUD para Usuarios.

class CriaUsuario(CreateView):
    model = Usuario
    
    form_class = UsuarioForm
    template_name = 'cria_usuario.html'
    context_object_name = 'CriaUsuario'
    success_url = reverse_lazy('avaliador:listar')
    
    
class ListarUsuario(ListView):
    model = Usuario
    
    template_name = ('lista_usuario.html')
    context_object_name = 'usuarios'
    
class DeletaUsuario(DeleteView):
    model = Usuario
    
    success_url = reverse_lazy('avaliador:listar')
    template_name = 'confirmar_delete.html'
    context_object_name = 'usuarios'
    
class AtualizarUsuario(UpdateView):
    model = Usuario
    
    form_class = UsuarioForm
    context_object_name = 'usuarios'
    template_name = 'atualizar_usuario.html'
    success_url = reverse_lazy('avaliador:listar')
    

# CRUD para filmes.


class CriaFilme(CreateView):
    model = Filmes
   
    
    form_class = FilmeForm
    template_name = 'cria_filmes.html'
    context_object_name = 'CriaFilme'
    success_url = reverse_lazy('avaliador:listar_filme')
    
    def buscar_filmes(self, form):
        titulo = form.cleaned_data['titulo']
        dados_filme = buscador(titulo)
        if dados_filme:
            form.instance.titulo = dados_filme['titulo']
            form.instance.genero = dados_filme["genero"]
            form.instance.ano = dados_filme["ano"]
    def form_valid(self, form):
        self.buscar_filmes(form)

        if form.is_valid():
            return super().form_valid(form)

    
class ListarFilmes(ListView):
    model = Filmes
    
    template_name = ('lista_filmes.html')
    context_object_name = 'filmes' 
    
class DeletaFilmes(DeleteView):
    model = Filmes
    
    template_name = 'confirmar_delete_filmes.html'
    context_object_name = 'filmes'
    success_url = reverse_lazy('avaliador:listar_filme')
    
class AtualizarFilmes(UpdateView):
    model = Filmes
    
    form_class = FilmeForm
    context_object_name = 'filmes'
    template_name = 'atualizar_filmes.html'
    success_url = reverse_lazy('avaliador:listar_filme')