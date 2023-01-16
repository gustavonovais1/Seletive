# Seletive

<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://code.djangoproject.com/raw-attachment/tick   et/24953/django-hexbin.png" width="200" alt="Django Logo" /></a>
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>
</p>


<hr>

<a id="-tecnologias"></a>

## Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

<hr>

<a id="-projeto"></a>

## 💻 Projeto

Seletive é um sistema desenvolvido para a gerencia de candidaturas em vagas de emprego, nele é possível cadastrar/excluir empresas, adicionar vagas disponíveis, fazer filtros de empresas de acordo com as tecnologias utilizadas, criar tarefas para ser feitas durante o processo seletivo, e envio de emails para as empresas. 

<p align="center">
  <img alt="Página inicial" src="media/readme/pagina_inicial.jpg" width="100%">

  <img alt="Cadastro empresa" src="media/readme/cadastro_empresa.jpg" width="100%">

  <img alt="Página empresa" src="media/readme/pagina_empresa.jpg" width="100%">

  <img alt="Cadastro vaga" src="media/readme/cadastro_vaga.jpg" width="100%">

  <img alt="Pagina vaga" src="media/readme/pagina_vaga.jpg" width="100%">

  <img alt="Cadastro tarefa" src="media/readme/cadastro_tarefa.jpg" width="100%">

  <img alt="Envio de email" src="media/readme/envio_email_vaga.jpg" width="100%">
</p>

<a id="-como-executar"></a>

## 🚀 Como executar

### 💻 Pré-requisitos
 **Antes de começar, verifique se você atendeu aos seguintes requisitos:**

- Você tem uma máquina `< Windows / Linux / Mac >`.

- Você tem python na versão 3.11 ou superior instalado em sua máquina.


### Como instalar localmente:

- clone ou baixe o repositório.

```bash
# Clone este repositório
$ git clone https://github.com/gustavonovais1/Seletive.git

# Entre na pasta
$ cd Seletive
```

2 - inicie um ambiente virtual

```bash
# Criar
  # Linux
    $ python3 -m venv venv
  # Windows
    $ python -m venv venv


```
3 - Ativar
```bash

  # Linux
    $ source venv/bin/activate
  # Windows
    $ venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

  $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

```
3 - Configuração inicial
```bash

### Para total funcionamento da aplicação ainda é necessário fazer as migrações para gerar o esquema de banco de dados:

# Linux
python3 manage.py migrate
# Windows
python manage.py migrate

### Criando um usuário para acessar o painel de administração:

$ python3 .\manage.py createsuperuser
$ python .\manage.py createsuperuser

```
### 👨‍💻 Ativando a aplicação (localmente)

Para executar o servidor localmente (Com o ambiente virtual ativo):

```bash
# Linux
$ python3 manage.py runserver
# Windows
$ python manage.py runserver

Agora é possível acessar a aplicação em http://localhost:8000/
