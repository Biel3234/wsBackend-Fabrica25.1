from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields=['nome_usuario', 'email_usuario']
        
        labels={
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
        
        fields=['titulo', 'usuario', 'nota']
        
        labels={
            'titulo': 'Titulo do Filme',
            'nota': 'Nota de 0 a 10',
            'usuario': 'Email do Usuario',
        }
        widgets={
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
        }