# Aplicação com Django

### Sobre o projeto
Esse é um projeto prático avaliativo do segundo bimestre da disciplina <strong>Tópicos Especiais em Informática (Fatec)</strong> ministrada pelo professor <strong>Me. Fabrício Henrique</strong>.<br/><br/>
O aplicativo tem o tema de loja virtual para exibição de álbuns de músicas e filmes. Entre as tecnologias e linguagens utilizadas estão:
- <strong>Python</strong>
- <strong>Django</strong>
- <strong>HTML 5</strong>
- <strong>CSS 3</strong>
- <strong>Bootstrap 4</strong>
- <strong>Javascript</strong>
- <strong>JQuery</strong>
- <strong>PostgreSQL</strong>

### Alunos
- [André Luis da Silva](mailto:andre.silva316@fatec.sp.gov.br)<br/>
- [Diego Gabriel da Costa](https://github.com/DiegoCosta1)

# Como rodar a aplicação
## Instalações necessárias
#### [Download Python](https://www.python.org/downloads/)
#### [Download PostgreSQL](https://www.postgresql.org/download/)

É necessário que o computador tenha instalado Python e PostgreSQL ou algum outro SGBD.

#### Instalação do Django (Última versão estável - 3.2.9)
`pip install Django==3.2.9`

#### Instalar driver PostgreSQL no python
`pip install psycopg2`<br/>
`pip install psycopg2-binary`

#### Instalar form com estilização Bootstrap
`pip install django-bootstrap-form`<br/>
`pip install django-crispy-forms` <em>(não utilizado nesse projeto, opcional)</em>

## Criação do Database
É necessário a utilização de um <strong>database</strong> para o projeto.
A configuração do acesso ao banco é feita no arquivo <strong><em>[projeto_pratico/settings.py](https://github.com/DiegoCosta1/django-projeto_pratico_fatec/blob/main/projeto_pratico/settings.py#:~:text=ref/settings/%23databases-,DATABASES%20%3D%20%7B,%7D,-%23%20Password%20validation)</em></strong>.
As informações de <strong>NAME</strong>, <strong>USER</strong>, <strong>PASSWORD</strong> devem ser as mesmas do que o database criado. <strong>ENGINE</strong> também deverá ser alterado caso o banco não seja PostgreSQL.
<br/><br/>
Exemplo de configuração presente nesse arquivo:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE_NAME',
        'USER': 'USER_NAME',
        'PASSWORD': 'PASSWORD123',
        'HOST': 'localhost'
    }
}
```

## Gerenciamento do servidor Django
O arquivo [`manage.py`](https://github.com/DiegoCosta1/django-projeto_pratico_fatec/blob/main/manage.py) é utilizado para rodar vários comandos, entre eles: sincronização com o banco, criação de superuser e execução do servidor.<br/><br/>
Ele está localizado no diretório raiz do projeto e caso queria conhecer sua lista de comandos, ela pode ser exibida com:<br/>
django-projeto_pratico_fatec$ `python .\manage.py help`

#### Sincronizar banco de dados com o projeto e entidades
As migrações são importantes para manter os mesmos modelos entre a aplicação e banco sincronizados.<br/>
django-projeto_pratico_fatec$ `python .\manage.py makemigrations` <em>(Prepara as migrações necessárias)<br/></em>
django-projeto_pratico_fatec$ `python .\manage.py migrate` <em>(Realiza as migrações)</em>

#### Criação de super-usuário
Somente usuários cadastros terão acesso ao sistema. Porém, superusuários terão permissões administrativas, como acesso ao CRUD, exportação e importação de dados.<br/>
django-projeto_pratico_fatec$ `python .\manage.py createsuperuser`

#### Subir o servidor
django-projeto_pratico_fatec$ `python .\manage.py runserver`<br/>

Após a inicialização do servidor, podemos observar a seguinte mensagem que deve aparecer no terminal:<br/>
```
Django version 3.2.9, using settings 'projeto_pratico.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Nesse exemplo, o sistema pode ser acessado através do ip `localhost` com a porta `8000`. Ou seja, acessando o endereço [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) ou [`http://localhost:8000/`](http://localhost:8000/) com seu navegador.

#### Importar dados para o banco local
Após toda instalação, os dados podem ser copiados do arquivo [`data.json`](https://github.com/DiegoCosta1/django-projeto_pratico_fatec/blob/main/data.json) e utilizados no formulário de importação de dados: [`localhost:8000/import`](http://localhost:8000/import), para popular o banco de dados com exemplos de filmes e músicas.

# Curiosidades e outros comandos
#### Criação de um projeto com Django
`django-admin startproject projeto_pratico`

#### Coleção de arquivos static
A configuração dos <strong>arquivos estáticos</strong> (como CSS, JS, imagens, etc.) também são feitas no arquivo <em>[projeto_pratico/settings.py](https://github.com/DiegoCosta1/django-projeto_pratico_fatec/blob/main/projeto_pratico/settings.py#:~:text=STATIC_ROOT%20%3D%20os.path,%5D)</em>.<br/>
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'projeto_pratico/static')
]
```
Após a configuração, foi necessário rodar o comando abaixo para que os arquivos sejam coletados de todos os caminhos específicados:<br/>
django-projeto_pratico_fatec$ `python .\manage.py collectstatic`

#### Filosofias
##### [Django](https://docs.djangoproject.com/pt-br/2.2/misc/design-philosophies/)
##### [Python](https://www.python.org/dev/peps/pep-0020/)
