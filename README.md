# Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto localmente:

1. Clone o repositório do projeto:

    ```bash
    git clone https://github.com/SEU_USUARIO/projeto-estagio-django.git
    cd projeto-estagio-django
    ```

2. Crie um ambiente virtual para isolar as dependências do projeto:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - **Linux/Mac**:

      ```bash
      source venv/bin/activate
      ```

    - **Windows**:

      ```bash
      venv\Scripts\activate
      ```

4. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

5. Configure o banco de dados:

    Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o painel de administração:

    ```bash
    python manage.py createsuperuser
    ```

7. Execute o servidor local:

    ```bash
    python manage.py runserver
    ```

8. O servidor estará disponível em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

    Você pode acessar o painel de administração do Django em: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

9. Acesse o sistema usando:
    ```bash
    user = adm
    senha = adm
    ```

---