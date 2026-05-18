from django.shortcuts import render

from .models import Filme 


def home(request):
    
    filmes = Filme.objects.all()
    

    return render(request, 'index.html', {'filmes': filmes})