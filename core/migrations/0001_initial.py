# Generated by Django 2.2.7 on 2019-11-05 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('matricula', models.CharField(editable=False, max_length=8, verbose_name='Matricula')),
                ('cidade', models.CharField(max_length=40, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=20, verbose_name='Estado')),
                ('curso', models.CharField(max_length=200, verbose_name='Curso')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
