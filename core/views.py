from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Aluno, Certificado
from django.views.generic import View
from django.utils import timezone
from .render import Render


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
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']
        email = request.POST['email']
        newUser = User.objects.create_user(username=username, email=email, password=password)
        newUser.save()
        aluno = Aluno()
        aluno.nome = request.POST['nome']
        aluno.cidade = request.POST['cidade']
        aluno.uf = request.POST['estado']
        aluno.curso = request.POST['curso']
        aluno.user = User.objects.get(username=username)
        aluno.save()
        msg = 'true'
        return render(request, template_name, locals())
    return render(request, template_name)


@login_required()
def cadastro_certificado(request):
    template_name = 'cadastro_certificado.html'
    alunos = Aluno.objects.all()
    if request.method == 'POST':
        certificado = Certificado()
        certificado.faculdade = request.POST['faculdade']
        certificado.curso = request.POST['curso']
        certificado.carga_horaria = request.POST['carga']
        certificado.aluno = Aluno.objects.get(nome=request.POST['aluno'])
        certificado.save()
        msg = 'true'
        return render(request, template_name, locals())
    return render(request, template_name, locals())


@login_required()
def alunos(request):
    template_name = 'alunos.html'
    alunos = Aluno.objects.all()
    return render(request, template_name, locals())


@login_required()
def certificados(request):
    template_name = 'certificados.html'
    certificados = Certificado.objects.all()
    return render(request, template_name, locals())


class Pdf(View):

    def get(self, request, id):

        certificado = Certificado.objects.get(id=id)
        today = timezone.now()
        params = {
            'today': today,
            'certificado': certificado,
            'request': request
        }
        return Render.render('pdf.html', params)
