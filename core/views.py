from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

@login_required()
def index(request):
    grupo = Group.objects.get(name='professor')
    if grupo:
        template_name = 'index_professor.html'
        return render(request, template_name)


@login_required()
def cadastrar_aluno(request):
    template_name = 'teste.html'
    return render(request, template_name)
