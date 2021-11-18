from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('store_album', views.store_album, name='store_album'),
    path('store_movie', views.store_movie, name='store_movie'),
    
    # Autenticação
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    
    # Sobre
    path('sobre', views.sobre, name='sobre'),
    
    # Página de erro
    path('error', views.error_page, name='error_page'),

    # CRUD usuários
    path('list/user', views.list_user, name='list_user'),
    path('update/user/<int:id>/', views.update_user, name='update_user'),
    path('delete/user/<int:id>/', views.delete_user, name='delete_user'),

    # CRUD álbuns
    path('list/album', views.list_album, name='list_album'),
    path('create/album', views.create_album, name='create_album'),
    path('update/album/<int:id>/', views.update_album, name='update_album'),
    path('delete/album/<int:id>/', views.delete_album, name='delete_album'),

    # CRUD filmes
    path('list/movie', views.list_movie, name='list_movie'),
    path('create/movie', views.create_movie, name='create_movie'),
    path('update/movie/<int:id>/', views.update_movie, name='update_movie'),
    path('delete/movie/<int:id>/', views.delete_movie, name='delete_movie'),
]