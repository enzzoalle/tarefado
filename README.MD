# 📚 Tarefado

Aplicativo web acadêmico para organização de matérias, comentários, tarefas independentes e tarefas vinculadas a matérias com prazos de entrega.

---
## 🎯 Objetivo

Este é um projeto pessoal visando desenvolver um aplicativo web para ajudar estudantes a se organizarem academicamente. Serve também como portfólio técnico com foco em boas práticas.

---
## ✨ Funcionalidades

- **Matérias**  
  📘 Cadastro e visualização de disciplinas acadêmicas  
  💬 Sistema de comentários por matéria  

- **Tarefas**  
  ✅ Lista de tarefas independentes  
  📅 Tarefas vinculadas a matérias com prazos de entrega  

- **Dashboard**  
  📊 Visão geral do progresso acadêmico  

- **Segurança**  
  🔐 Autenticação de usuários

---
## 🛠 Como preparar o ambiente
### Configurar o ambiente virtual:
- Crie um ambiente virtual com o comando:
```bash
python -m venv venv
```
- Ative o ambiente virtual:
  - Windows:
  ```bash
  venv\Scripts\activate
  ```
  - Linux/Mac:
  ```bash
  source venv/bin/activate
    ```
- Instale as dependências:
```bash
pip install -r requirements.txt
```
- Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente conforme o exemplo em `.env.example`.
- Execute as migrações do banco de dados:
```bash
python manage.py migrate
```
- Crie uma secret key para o Django:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
- Cole a secret key no arquivo `.env` na variável `KEY_MY_DJANGO`.

---
### Criar o banco de dados PostgreSQL:
- Abra o pgAdmin, abra um novo query tool e execute o comando:
```sql
CREATE ROLE dev WITH 
    SUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    LOGIN
    NOREPLICATION
    NOBYPASSRLS
    CONNECTION LIMIT -1;
```
- Agora defina uma senha para o usuário `dev`:
```sql
ALTER ROLE dev WITH PASSWORD 'password';
```
- Agora crie um banco de dados chamado `dev_tarefado` e atribua o owner `dev`.
- Agora vincule os dados do banco de dados no arquivo `.env` (veja o exemplo em `.env.example`).

---
### Crie uma Senha de App para envio de e-mails 
- Se o projeto envia e-mails usando o Gmail/Google, você não deve usar sua senha principal. Crie uma "Senha de App" específica para ele:
    * Acesse sua Conta Google: [myaccount.google.com](https://myaccount.google.com/)
    * Vá para `Segurança`.
    * Em "Como fazer login no Google", clique em `Verificação em duas etapas` (ela precisa estar ativada).
    * Na parte inferior, clique em `Senhas de app`.
    * Selecione "E-mail" como o app e "Computador Windows/Mac" como o dispositivo, dê um nome (ex: "Projeto Tarefado") e clique em "Gerar".
    * Copie a senha de 16 dígitos gerada (sem os espaços) e cole na variável `MY_EMAIL_PASS`.
--- 
- Crie um superusuário para acessar o admin do Django:
```bash
python manage.py createsuperuser
```
- Agora você pode rodar o servidor de desenvolvimento normalmente:
```bash
python manage.py runserver
```
