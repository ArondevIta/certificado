from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Aluno, Certificado
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile



@login_required()
def index(request):
    try:
        grupo = Group.objects.get(user=request.user)
        if grupo:
            template_name = 'index_professor.html'

            # if query:
            #     certificados = certificados.filter(codigo__icontains=query) | \
            #                    certificados.filter(aluno__icontains=query) | \
            #                    certificados.filter(faculdade__icontains=query)
            #     msg = 'pesquisa'
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
        certificado.coordenador = request.POST['coordenador']
        certificado.aluno = Aluno.objects.get(nome=request.POST['aluno'])
        certificado.save()
        msg = 'true'
        return render(request, template_name, locals())
    return render(request, template_name, locals())


@login_required()
def alunos(request):
    template_name = 'alunos.html'
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, template_name, locals())


@login_required()
def certificados(request):
    template_name = 'certificados.html'
    certificados = Certificado.objects.all()
    return render(request, template_name, locals())


@login_required()
def pdf(request, id):
    """Generate pdf."""
    # Model data
    certificado = Certificado.objects.get(id=id)

    response = HttpResponse(content_type="application/pdf")
    html = render_to_string("pdf.html", {
        'certificado': certificado,
    })

    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
    # HTML(string=html).write_pdf(response)
    return response


@login_required()
def aluno_certificado(request):
    template_name = 'aluno_certificado.html'
    aluno = Aluno.objects.get(user=request.user)
    certificados = Certificado.objects.filter(aluno=aluno)
    # query = request.GET.get('q')
    if request.method == 'POST':
        query = request.POST['q']
        if query:
            certificados = Certificado.objects.filter(codigo=query)
            if certificados:
                msg = 'existe'
                return render(request, template_name, locals())
            else:
                msg = 'false'
                return render(request, template_name, locals())
    return render(request, template_name, locals())


@login_required()
def aluno_dados(request):
    template_name = 'aluno_dados.html'
    aluno = Aluno.objects.get(user=request.user)
    return render(request, template_name, locals())

@login_required()
def aluno_update(request, id):
    user = Aluno.objects.get(user=request.user)

    if request.method == 'POST':
        aluno = Aluno.objects.get(id=id)
        aluno.nome = request.POST['aluno_Nome']
        aluno.matricula = request.POST['aluno_Matricula']
        aluno.cidade = request.POST['aluno_Cidade']
        aluno.uf = request.POST['aluno_Estado']
        aluno.curso = request.POST['cidade_Empresa']
        aluno.save()
        return redirect('aluno_dados')
