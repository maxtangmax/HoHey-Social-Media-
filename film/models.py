from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image





class film_profile(models.Model):
	film_name= models.CharField(max_length=100, unique=True)
	film_summary = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	film_image = models.ImageField(default='default.jpg', upload_to='film_profile')

	def __str__(self):
		return self.film_name