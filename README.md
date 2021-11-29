# Aplicação com Django
Esse é um projeto prático avaliativo do segundo bimestre da disciplina <strong>Tópicos Especiais em Informática (Fatec)</strong> ministrada pelo professor <strong>Me. Fabrício Henrique</strong>. Foi utilizado um tema de loja para exibição de dados com a linguagem de programação <strong>Python</strong> integrado com banco de dados <strong>PostgreSQL</strong> e interfaces <strong>web</strong>.<br/>
Aluno: [Diego Costa](https://github.com/DiegoCosta1).

## Como subir o servidor Django
O arquivo `manage.py` é utilizado para rodar vários comandos, incluse para poder subir o servidor, como no exemplo abaixo:
`projeto_pratico> python .\manage.py runserver` <em>(obs.: é importante o cmd/terminal estar localizado no diretório <em>projeto_pratico</em> ou então precisará especificar o caminho direto para o arquivo manage.py)</em><br/><br/>
Caso queira conhecer a lista de comandos disponíveis peça uma ajuda ao python:<br/>
`projeto_pratico> python .\manage.py help`

Após a inicialização do servidor, podemos observar a seguinte mensagem que deve aparecer no terminal:<br/>
```
Django version 3.2.9, using settings 'projeto_pratico.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Nesse exemplo, o sistema pode ser acessado através do ip `localhost` com a porta `8000`. Ou seja, acessando o endereço [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) ou [`http://localhost:8000/`](http://localhost:8000/) com seu navegador.

## Instalações e Configurações
A configuração do <strong>banco de dados</strong> é feita no arquivo <em>projeto_pratico/settings.py</em>.<br/>
Pode ser necessário alterar algumas informações, como o nome do banco, usuário e senha. Se for utilizado algum banco diferente do PostgreSQL, também pode ser necessário mudar a engine usada por padrão.<br/>
Exemplo de configuração presente nesse arquivo:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE_NAME',
        'USER': 'USER_NAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost'
    }
}
```

### Sincronizar banco de dados com o projeto e entidades (models.py)
`projeto_pratico> python .\manage.py makemigrations` <em>(Prepara as migrações necessárias)<br/></em>
`projeto_pratico> python .\manage.py migrate` <em>(Realiza as migrações)</em>

### Criação de super-usuário
Somente usuários cadastros terão acesso ao sistema. Superusuários tem permissões especiais, como por exemplo acesso ao CRUD de produtos.<br/>
`projeto_pratico> python .\manage.py createsuperuser`

### Coleção de arquivos static
A configuração dos <strong>arquivos estáticos</strong> (como CSS, JS, imagens, etc.) também são feitas no arquivo <em>projeto_pratico/settings.py</em>.<br/>
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'projeto_pratico/static')
]
```
Após a configuração, é necessário rodar o comando abaixo para que os arquivos sejam coletados de todos os caminhos específicados na configuração:<br/>
`python .\manage.py collectstatic`

### Comandos usados para instalação de dependencias e criação do projeto
#### Instalação do Django (Última versão estável - 3.2.9)
`pip install Django==3.2.9`

#### Instalar driver PostgreSQL no python
`pip install psycopg2`<br/>
`pip install psycopg2-binary`


#### Instalar form com estilização Bootstrap
`pip install django-bootstrap-form`<br/>
`pip install django-crispy-forms` <em>(segunda alternativa, opcional)</em>

#### Inicio do projeto com Django
`django-admin startproject projeto_pratico`

### Links externos para download
#### [Download Python](https://www.python.org/downloads/)
#### [Download PostgreSQL](https://www.postgresql.org/download/)

### Curiosidades
#### [Filosofia Django](https://docs.djangoproject.com/pt-br/2.2/misc/design-philosophies/)
#### [Filosofia Python](https://www.python.org/dev/peps/pep-0020/)