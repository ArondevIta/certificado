from django.contrib import admin
from django.urls import path
from .views import cadastrar_aluno,\
    index, \
    cadastro_certificado, \
    alunos, \
    certificados, \
    pdf, aluno_certificado, \
    aluno_dados,  aluno_update, home, edit_aluno, alterar_senha, excluir_aluno


urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('alunos', alunos, name='alunos'),
    path('aluno_certificado', aluno_certificado, name='aluno_certificado'),
    path('aluno_dados', aluno_dados, name='aluno_dados'),
    path('aluno_update/<int:id>', aluno_update, name='aluno_update'),
    path('alterar_senha/<int:id>', alterar_senha, name='alterar_senha'),
    path('cadastro', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastro_certificado', cadastro_certificado, name='cadastrar_certificado'),
    path('certificados', certificados, name='certificados'),
    path('editar_aluno/<int:id>', edit_aluno, name='edit_aluno'),
    path('excluir_aluno/<int:id>', excluir_aluno, name='excluir_aluno'),
    path('pdf/<int:id>', pdf, name='pdf'),
]
