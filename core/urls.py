from django.contrib import admin
from django.urls import path
from .views import cadastrar_aluno, index, cadastro_certificado, alunos, certificados, pdf


urlpatterns = [
    path('', index, name='index'),
    path('alunos', alunos, name='alunos'),
    path('cadastro', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastro_certificado', cadastro_certificado, name='cadastrar_certificado'),
    path('certificados', certificados, name='certificados'),
    path('pdf/<int:id>', pdf, name='pdf'),
]
