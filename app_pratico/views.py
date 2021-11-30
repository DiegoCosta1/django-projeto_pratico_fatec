import io, json, zipfile
from zipfile import ZipFile
from django.db import models
from django.db.models.query import InstanceCheckMeta
from django.http.request import validate_host
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core import serializers
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib import admin, auth, messages
from datetime import datetime
from app_pratico.models import Album, Movie
from .forms import UserForm, AlbumForm, MovieForm
# Create your views here.

# INDEX
@login_required(login_url='login')
def index(request):
    albums = Album.objects.all().filter(year=datetime.now().year).order_by('title')
    movies = Movie.objects.all().filter(year=datetime.now().year).order_by('title')

    context = {
        'albums' : albums,
        'movies' : movies,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def store_album(request):
    albums = Album.objects.all().order_by('artist', '-year')

    context = {
        'albums' : albums,
    }
    return render(request, 'store/album.html', context)
    
@login_required(login_url='login')
def store_movie(request):
    movies = Movie.objects.all().order_by('director', '-year')

    context = {
        'movies' : movies,
    }
    return render(request, 'store/movie.html', context)

# SOBRE
@login_required(login_url='login')
def sobre(request):
    return render(request, 'sobre.html')

# LOGIN USUÁRIO
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        # Validações
        if isEmpty(username):
            messages.error(request,'Erro: o nome não pode ficar vazio')
            return redirect('login')
        if isEmpty(password):
            messages.error(request,'Erro: as senhas não podem ficar vazias')
            return redirect('login')
        if not User.objects.filter(username=username).exists():
            messages.warning(request,'Atenção: usuário não existe')
            return redirect('login')

        user = auth.authenticate(username=username, password=password)

        if user is None:
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('/index')

    else:
        return render(request, 'login.html')

# LOGOUT USUÁRIO
def logout(request):
    auth.logout(request)
    return redirect('index')

# CRIAR USUÁRIO
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validações
        if isEmpty(username) or isEmpty(first_name):
            messages.error(request,'Erro: o nome não pode ficar vazio')
            return redirect('signup')
        if isEmpty(email):
            messages.error(request,'Erro: o e-mail não pode ficar vazio')
            return redirect('signup')
        if isEmpty(password) or isEmpty(password2):
            messages.error(request,'Erro: as senhas não podem ficar vazias')
            return redirect('signup')
        if password != password2:
            messages.error(request,'Erro: as senhas não são iguais')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Atenção: nome de usuário já cadastro')
            return redirect('signup')

        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
        user.save()
        messages.success(request, 'Registrado com sucesso')
        return redirect('login')
    return render(request, 'signup.html')

# CRUD USUÁRIO
@staff_member_required(login_url='login')
def list_user(request):
    users = User.objects.all().order_by('id')
    return render(request, 'list/user.html', {'users' : users})

@staff_member_required(login_url='login')
def update_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(instance=user)

    if (request.method == 'POST'):
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            # user.password = form.cleaned_data['password']
            user.first_name = form.cleaned_data['first_name']
            user.email = form.cleaned_data['email']

            user.save()
            return redirect('list_user')

    context = {
        'form': form,
    }
    return render(request, 'form/user.html', context)

@staff_member_required(login_url='login')
def delete_user(request, id):
    user = User.objects.get(id=id)
    username = user.username

    # if request.method == 'POST':
    user.delete()
    
    messages.success(request, 'Usuário "'+ username +'" removido com sucesso')
    return redirect('list_user')
    
    # return render(request, 'delete-confirm.html', {'user': user})

# CRUD ÁLBUM
@staff_member_required(login_url='login')
def list_album(request):
    albums = Album.objects.all().order_by('id')

    context = {
        'albums' : albums,
    }
    return render(request, 'list/album.html', context)

@staff_member_required(login_url='login')
def create_album(request):
    form = AlbumForm(request.POST or None)

    if (request.method == 'POST') and (form.is_valid()):
        album = form.save(commit=False)
        album.title = form.cleaned_data['title']
        album.artist = form.cleaned_data['artist']
        album.art = form.cleaned_data['art']
        album.genre = form.cleaned_data['genre']
        album.price = form.cleaned_data['price']
        album.year = form.cleaned_data['year']

        album.save()
        return redirect('list_album')

    context = {
        'form': form,
    }

    return render(request, 'form/album.html', context)

@staff_member_required(login_url='login')
def update_album(request, id):
    album = get_object_or_404(Album, pk=id)
    form = AlbumForm(instance=album)

    if (request.method == 'POST'):
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.title = form.cleaned_data['title']
            album.artist = form.cleaned_data['artist']
            album.art = form.cleaned_data['art']
            album.genre = form.cleaned_data['genre']
            album.price = form.cleaned_data['price']
            album.year = form.cleaned_data['year']

            album.save()
            return redirect('list_album')

    context = {
        'form': form,
    }

    return render(request, 'form/album.html', context)

@staff_member_required(login_url='login')
def delete_album(request, id):
    album = Album.objects.get(id=id)
    title = album.title

    album.delete()

    messages.success(request, 'Álbum "'+ title +'" removido com sucesso')
    return redirect('list_album')

# CRUD FILME
@staff_member_required(login_url='login')
def list_movie(request):
    movies = Movie.objects.all().order_by('id')

    context = {
        'movies' : movies,
    }
    return render(request, 'list/movie.html', context)

@staff_member_required(login_url='login')
def create_movie(request):
    form = MovieForm(request.POST or None)

    if (request.method == 'POST') and (form.is_valid()):
        movie = form.save(commit=False)
        movie.title = form.cleaned_data['title']
        movie.artist = form.cleaned_data['director']
        movie.art = form.cleaned_data['art']
        movie.genre = form.cleaned_data['genre']
        movie.price = form.cleaned_data['price']
        movie.year = form.cleaned_data['year']

        movie.save()
        return redirect('list_movie')

    context = {
        'form': form,
    }

    return render(request, 'form/movie.html', context)

@staff_member_required(login_url='login')
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(instance=movie)

    if (request.method == 'POST'):
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.title = form.cleaned_data['title']
            movie.director = form.cleaned_data['director']
            movie.art = form.cleaned_data['art']
            movie.genre = form.cleaned_data['genre']
            movie.price = form.cleaned_data['price']
            movie.year = form.cleaned_data['year']

            movie.save()
            return redirect('list_movie')

    context = {
        'form': form,
    }

    return render(request, 'form/movie.html', context)

@staff_member_required(login_url='login')
def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    title = movie.title

    movie.delete()

    messages.success(request, 'Álbum "'+ title +'" removido com sucesso')
    return redirect('list_movie')

@staff_member_required(login_url='login')
def export_all_data(request):
    # Lista de todos modelos
    Album_serialize = serializers.serialize("json", Album.objects.all().order_by('id'))

    Movie_serialize = serializers.serialize("json", Movie.objects.all().order_by('id'))

    User_serialize = serializers.serialize("json", User.objects.all().order_by('id'))

    # Data em formato json
    data = {
        "Album" : json.loads(Album_serialize),
        "Movie" : json.loads(Movie_serialize),
        "User" : json.loads(User_serialize),
        "Data de exportação" : datetime.now().isoformat()
    }

# todo: downloading corrupted ZIP File
    # Arquivo binário
    # in_memory_zip = io.BytesIO()

    # with ZipFile(in_memory_zip, mode='w') as zip_file:
    #     with zip_file.open("data.json", 'w') as json_file:
    #         data_bytes = json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8')
    #         json_file.write(data_bytes)
    
    # response = HttpResponse(in_memory_zip, content_type='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename="%s"' % 'dados_exportados.zip'

    response = HttpResponse(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'), 
        content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'dados_exportados.js'

    return JsonResponse(data)
    # return response

@staff_member_required(login_url='login')
def import_json_data(request):
    return render(request, 'errorPage.html')

def error_page(request):
    return render(request, 'errorPage.html')

def isEmpty(str):
    return not str.strip()