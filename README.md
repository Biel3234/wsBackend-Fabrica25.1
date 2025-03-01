# 🎮 Avaliador de Filmes

Este projeto é uma aplicação web desenvolvida com **Django** que permite aos usuários cadastrar, listar e avaliar filmes. A aplicação oferece um CRUD completo para filmes e usuários, além de uma interface amigável para interação.

## 🚀 Funcionalidades

- **Cadastro de Usuários:** Permite o registro de novos usuários com nome e e-mail.
- **Cadastro de Filmes:** Usuários podem adicionar novos filmes com título, gênero, ano e nota.
- **Listagem de Filmes:** Exibe uma lista de filmes cadastrados com suas respectivas informações.
- **Edição e Exclusão:** Funcionalidades para editar ou remover filmes e usuários.
- **Avaliações:** Usuários podem atribuir notas aos filmes.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django**
- **SQLite** (banco de dados padrão)

## 📺 Estrutura do Projeto

```bash
wsBackend-Fabrica25.1/
├── app_avalia_filmes/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   ├── templates/
│   │   ├── base.html
│   │   ├── cria_filmes.html
│   │   ├── lista_filmes.html
│   │   └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── projeto_avalia_filmes/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Biel3234/wsBackend-Fabrica25.1.git
   cd wsBackend-Fabrica25.1
   ```

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv venv
   # Ative no Windows
   venv\Scripts\activate
   # Ative no Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional, para acessar o admin do Django):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   Acesse a aplicação em `http://127.0.0.1:8000/`.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por Antonio Gabriel 🎸

