from django.contrib import admin
from .models import Aluno, Certificado

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'matricula',
        'cidade',
        'uf',
        'curso',
        'user'
    ]


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = [
        'aluno',
        'codigo',
        'faculdade',
        'curso',
        'carga_horaria',
        'coordenador',
        'criado_em'
    ]
