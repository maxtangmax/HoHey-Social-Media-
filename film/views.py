from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FilmRegisterForm, FilmProfileUpdateForm, FilmSummaryUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import film_profile
from .filters import film_profile_filter
from django.views.generic import (ListView, 
                                    DetailView, 
                                    UpdateView, 
                                    CreateView)


@login_required
def register(request):
    if request.method == "POST":
        form = FilmRegisterForm(request.POST)
        if form.is_valid():
        	form.instance.author = request.user
        	form.save()
        	film_name = form.cleaned_data.get('film_name')
        	messages.success(request, f'The profile for {film_name} is created on HoHey!')
        	return redirect('film_profile')
    else:
        form = FilmRegisterForm()
    return render(request, 'film_register.html', {'form': form})

def update_profile(request):
    if request.method == "POST":
        u_form = FilmSummaryUpdateForm(request.POST, 
                                       ) #request.film_image
        p_form = FilmProfileUpdateForm(request.POST, 
                                       request.FILES, 
                                       )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'The profile for {film_name} is updated on HoHey!')
            return redirect("film_profile")
    else:
        u_form = FilmSummaryUpdateForm()
        p_form = FilmProfileUpdateForm()
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'films': film_profile.objects.all()
    }
    return render(request, 'film_update.html', context)



def view_profile(request):
    films=film_profile.objects.all()
    myFilter=film_profile_filter(request.GET, queryset=films)

    films=myFilter.qs


    context = {
        'films': films,
        'myFilter':myFilter
    }
    return render(request, 'film_profile.html', context)

class PostDetailView(DetailView):
    model=film_profile
    template_name='film_profile_detail.html'
    #<app>/<model>_<viewtype>.html




