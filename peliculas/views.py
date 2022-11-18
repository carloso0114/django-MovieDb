from django.shortcuts import render
from django.views import generic
from .models import Director, Pelicula

# Create your views here.
def index(request):
  num_books = 'a'
  return render(
    request, 
    'index.html',
    context={
      'num_books': num_books
    }
  )

class IndexView(generic.ListView):
    template_name = 'directores.html'
    model = Director

class DirectorView(generic.DetailView):
    template_name = 'director.html'
    model = Director

class PeliculasView(generic.ListView):
    template_name = 'peliculas.html'
    model = Pelicula

class PeliculaView(generic.DetailView):
    template_name = 'pelicula.html'
    model = Pelicula


  