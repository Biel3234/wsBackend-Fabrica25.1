from django.db import models

class Usuario(models.Model):
    
    nome_usuario = models.CharField(max_length=30)
    email_usuario = models.EmailField(unique=True)

    def __str__(self):
        return f"Usuário: {self.nome_usuario}"
    
class Filmes(models.Model):
    
    
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=40)
    ano = models.CharField(max_length=4)
    nota = models.DecimalField(decimal_places=1, max_digits=3)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='email_usuario')
    
    
    def __str__(self):
        return f"Filme: {self.titulo}"
