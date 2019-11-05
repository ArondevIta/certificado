from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


@login_required()
def index(request):
    try:
        grupo = Group.objects.get(user=request.user)
        if grupo:
            template_name = 'index_professor.html'
            return render(request, template_name)
    except:
        template_name = 'index_aluno.html'
        return render(request, template_name)


@login_required()
def cadastrar_aluno(request):
    template_name = 'cadastro.html'
    return render(request, template_name)
