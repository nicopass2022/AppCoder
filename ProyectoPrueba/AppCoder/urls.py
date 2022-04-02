
from django.urls import path
from .views import curso, estudiantes, entregables, inicio, profesores

urlpatterns = [
    path('', inicio),
    path('agrega-curso/<nombre>/<camada>', curso),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('familiar/', entregables),
    
]

