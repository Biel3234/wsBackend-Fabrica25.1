from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields=['nome_usuario', 'email_usuario']
        
        label={
            'nome_usuario': 'Nome do Usuario',
            'email_usuario': 'Email do Usuario',
        }
        widgets={
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'email_usuario': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filmes
        
        fields=['titulo', 'genero', 'ano', 'usuario']
        
        label={
            'titulo': 'Titulo do Filme',
            'genero': 'Genero do Filme',
            'ano': 'Ano de lançamento',
            'usuario': 'Usuario',
        }
        widgets={
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
        }