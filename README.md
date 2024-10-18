# Gerenciador de Tarefas - API REST

### 🚀 **Sobre o Projeto**
Este projeto é minha resolução para um desafio proposto: Criar uma API REST para gerenciar tarefas, contendo autenticação de usuários e manipulação de tarefas de forma simples. Ideal para pessoas que precisam de uma solução rápida e prática para organização de atividades.

---

## 🛠 **Tecnologias Utilizadas**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python version">
  <img src="https://img.shields.io/badge/Flask-2.0+-red.svg" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-5.7+-blue.svg" alt="MySQL">
  <img src="https://img.shields.io/badge/Flask--MySQLdb-1.4+-green.svg" alt="Flask-MySQLdb">
  <img src="https://img.shields.io/badge/JWT-Auth-green.svg" alt="JWT Authentication">
</p>

---

## **Endpoints**

### **Usuário**
- `POST /register` - Cria um novo usuário.
- `POST /login` - Autentica o usuário e retorna um token JWT.

### **Tarefas**
- `POST /task` - Adiciona uma nova tarefa.
- `PUT /task/<int:id>` - Atualiza uma tarefa.
- `GET /task/<int:id>` - Visualiza uma tarefa específica.
- `GET /task/all` - Lista todas as tarefas do usuário autenticado.
- `DELETE /task/<int:id>` - Exclui uma tarefa.

---

## ⚙️ **Como Executar**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-tarefas.git
   cd gerenciador-tarefas
   ```
2. Crie um ambiente virtual e ative-o:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```
    pip install -r requirements.txt
    ```
5. Configure o banco de dados MySQL no arquivo db_config.py.
6. Inicialize as tabelas executando o script:
   ```
   python3 db_model.py
   ```
7. Inicie a aplicação:
   ```
   python3 app.py
   ```


## 🌱 **Próximos Passos**
Implementar uma interface visual (HTML, CSS, JS) para facilitar o uso da API.
Hospedar a aplicação em uma plataforma de nuvem (como AWS, Heroku ou Railway) para torná-la acessível publicamente.

## 🎯 **Considerações Finais**
Este projeto fornecer uma solução, de muitas possíveis, simples, funcional e escalável para gerenciamento de tarefas. 

Desenvolvido em Python, utilizando um framework web amplamente utilizado no mercado de trabalho:Flask e manipulando dados através do MySQL, este projeto pode ser o ponto de partida para aplicações maiores ou serr utilizado como exemplo de aprendizado em APIs RESTful.

