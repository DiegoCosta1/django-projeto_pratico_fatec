from django import forms
from django.contrib.auth.models import User
from .models import Album, Movie

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'art', 'genre', 'price', 'year']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'art', 'genre', 'price', 'year']
        