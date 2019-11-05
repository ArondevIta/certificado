from django.db import models
from django.contrib.auth.models import User
import uuid

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=200)
    matricula  = models.CharField('Matricula', max_length=8, editable=False)
    cidade = models.CharField('Cidade', max_length=40)
    uf = models.CharField('Estado', max_length=20)
    curso = models.CharField('Curso', max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def save(self):
        self.subscription = str(uuid.uuid4().time_low)[:6]
        super(Aluno, self).save()


class Certificado(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False)
    faculdade = models.CharField('Instituição de ensino', max_length=150)
    curso = models.CharField('Curso', max_length=200)
    carga_horaria = models.IntegerField('Carga Horaria')

    def __str__(self):
        return self.codigo
