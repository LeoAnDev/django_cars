# django_cars
Projeto Django Cars

# Criar o ambiente virtual
py -m venv venv

# Ativar o ambiente virtual
.\venv\Scripts\activate

# Instalar o Django
pip install django

# Atualizar o pip
python.exe -m pip install --upgrade pip

# Saber versão do Django
django-admin --version

# Saber versão do pip
pip --version

# Saber versão do Python
py --version

# Criando o projeto principal (core)
django-admin startproject app .

# Subir o servidor
py manage.py runserver

# Subir as migrations nativas
py manage.py migrate

# Subir minhas migrations
py manage.py makemigrations

# Criar superusuario
py manage.py createsuperuser

# Criar aplicação
py manage.py startapp cars

# Instalar a biblioteca dotenv
pip install python-dotenv

# Permitir quais fontes pode acessar
pip install django-csp