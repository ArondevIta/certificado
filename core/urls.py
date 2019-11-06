from django.contrib import admin
from django.urls import path
from .views import cadastrar_aluno, index, cadastro_certificado, alunos


urlpatterns = [
    path('alunos', alunos, name='alunos'),
    path('cadastro', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastro_certificado', cadastro_certificado, name='cadastrar_certificado'),
    path('index', index, name='index')
]