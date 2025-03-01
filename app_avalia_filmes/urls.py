from django.urls import path,include
from .views import *

app_name = 'avaliador'

urlpatterns = [
    path('criar/', CriaUsuario.as_view() , name='criar'),
    path('sucesso/', usuario_sucesso, name='sucesso'),
    path('listar/', ListarUsuario.as_view(), name='listar'),
    path('deletar/<int:pk>', DeletaUsuario.as_view(), name='deletar'),
    path('atualizar/<int:pk>', AtualizarUsuario.as_view(), name='atualizar'),
    
    path('criar_filme/', CriaFilme.as_view() , name='criar_filme'),
    # path('sucesso/', usuario_sucesso, name='sucesso'),
    path('listar_filme/', ListarFilmes.as_view(), name='listar_filme'),
    path('deletar_filme/<int:pk>', DeletaFilmes.as_view(), name='deletar_filme'),
    path('atualizar_filme/<int:pk>', AtualizarFilmes.as_view(), name='atualizar_filme'),
]