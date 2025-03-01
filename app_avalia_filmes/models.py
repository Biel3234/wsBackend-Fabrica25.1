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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='email_usuario')
    
    def __str__(self):
        return f"Filme: {self.titulo}"

    
class Avaliacao(models.Model):
    
    
    filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field='email_usuario') 
    avaliacao = models.TextField()
    
    def __str__(self):
        return f"{self.filme.titulo}' avaliado pelo usuario {self.usuario.nome_usuario}"