from django import forms
from django.contrib.auth.models import User
from .models import film_profile
from django.forms import ModelForm

class FilmRegisterForm(ModelForm):
    class Meta:
        model = film_profile
        fields = ['film_name', 'film_summary', 'film_image', 'Director',
				'Producer',
				'Writer',
				'Editor',
				'Cinematographer',
				'Production_Designer',
				'Art_Director',
				'Visual_effects',
				'Costume',
				'Casting',
				'Music',
				'Set_direction',
				'Studio',
				'Year',
				'Language',
				'Actors']



class FilmProfileUpdateForm(ModelForm):
	class Meta:
		model = film_profile
		fields = ['film_image']


class FilmSummaryUpdateForm(ModelForm):
	class Meta:
		model = film_profile
		fields = ['film_summary']



