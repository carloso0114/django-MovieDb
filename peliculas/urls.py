from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('directores', views.IndexView.as_view(), name='lista_directores'),
  path('director/<pk>', views.DirectorView.as_view(), name='detalle_director'),
  path('peliculas', views.PeliculasView.as_view(), name='lista_peliculas'),
  path('pelicula/<pk>', views.PeliculaView.as_view(), name='detalle_pelicula'),
]