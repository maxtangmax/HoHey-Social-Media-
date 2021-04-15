from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FilmRegisterForm
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = FilmRegisterForm(request.POST)
        if form.is_valid():
        	form.instance.author = request.user
        	form.save()
        	film_name = form.cleaned_data.get('film_name')
        	messages.success(request, f'The profile for {film_name} is created on HoHey!')
        	return redirect('blog-home')
    else:
        form = FilmRegisterForm()
    return render(request, 'film_register.html', {'form': form})

# Create your views here.
