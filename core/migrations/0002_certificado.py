# Generated by Django 2.2.7 on 2019-11-05 01:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('faculdade', models.CharField(max_length=150, verbose_name='Instituição de ensino')),
                ('curso', models.CharField(max_length=200, verbose_name='Curso')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horaria')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Aluno')),
            ],
        ),
    ]
