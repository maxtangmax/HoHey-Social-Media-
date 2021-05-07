from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class film_profile(models.Model):
	film_name= models.CharField(max_length=100, unique=True)
	film_summary = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	film_image = models.ImageField(default='default.jpg', upload_to='film_profile')
	Director=models.CharField(max_length=100, default="")
	Producer= models.CharField(max_length=100, default="")
	Writer= models.CharField(max_length=100, blank=True)
	Editor = models.CharField(max_length=100, blank=True)
	Cinematographer=models.CharField(max_length=100, blank=True)
	Production_Designer=models.CharField(max_length=100, blank=True)
	Art_Director=models.CharField(max_length=100, blank=True)
	Visual_effects= models.TextField(blank=True)
	Costume= models.TextField(blank=True)
	Make_up=models.TextField(blank=True)
	Casting=models.TextField(blank=True)
	Music=models.TextField(blank=True)
	Set_direction=models.TextField(blank=True)
	Studio = models.CharField(max_length=100, blank=True)
	Year = models.IntegerField(validators=[max_value_current_year], default="2000")
	Language = models.CharField(max_length=100, default="")
	Actors = models.TextField(default="")






	def __str__(self):
		return self.film_name


	



