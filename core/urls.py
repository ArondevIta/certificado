from django.contrib import admin
from django.urls import path
from .views import cadastrar_aluno, index


urlpatterns = [
    path('cadastro', cadastrar_aluno, name='cadastrar_aluno'),
    path('index', index, name='index')
]