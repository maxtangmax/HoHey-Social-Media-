from django import forms
from django.contrib.auth.models import User
from .models import film_profile
from django.forms import ModelForm

class FilmRegisterForm(ModelForm):
    class Meta:
        model = film_profile
        fields = ['film_name', 'film_summary', 'film_image']