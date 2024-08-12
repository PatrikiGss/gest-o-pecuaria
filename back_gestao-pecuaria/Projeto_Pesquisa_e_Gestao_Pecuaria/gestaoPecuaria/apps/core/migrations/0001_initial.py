# Generated by Django 5.1 on 2024-08-11 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cultura',
                'verbose_name_plural': 'Culturas',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Laboratório',
                'verbose_name_plural': 'Laboratórios',
            },
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Produtor',
                'verbose_name_plural': 'Produtores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=128)),
                ('creditos', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('produtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produtor')),
            ],
            options={
                'verbose_name': 'Propriedade',
                'verbose_name_plural': 'Propriedades',
            },
        ),
        migrations.CreateModel(
            name='AnaliseSolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('gleba', models.CharField(max_length=255)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laudo', models.TextField()),
                ('ph_h2o', models.DecimalField(decimal_places=2, max_digits=5)),
                ('s', models.DecimalField(decimal_places=2, max_digits=5)),
                ('p', models.DecimalField(decimal_places=2, max_digits=5)),
                ('k', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ca', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('na', models.DecimalField(decimal_places=2, max_digits=5)),
                ('al', models.DecimalField(decimal_places=2, max_digits=5)),
                ('h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('materia_organica', models.DecimalField(decimal_places=2, max_digits=5)),
                ('areia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('silte', models.DecimalField(decimal_places=2, max_digits=5)),
                ('argila', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mn', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fe', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cu', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zn', models.DecimalField(decimal_places=2, max_digits=5)),
                ('b', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cultura')),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.laboratorio')),
                ('propriedade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.propriedade')),
            ],
            options={
                'verbose_name': 'Análise de Solo',
                'verbose_name_plural': 'Análises de Solo',
            },
        ),
        migrations.CreateModel(
            name='Recomendacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camada_correcao', models.CharField(max_length=255)),
                ('calcario_calcitico', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcario_dolomitico', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcario_magnesiano', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gesso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kcl', models.DecimalField(decimal_places=2, max_digits=5)),
                ('p2o5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('n', models.DecimalField(decimal_places=2, max_digits=5)),
                ('s', models.DecimalField(decimal_places=2, max_digits=5)),
                ('analise_solo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.analisesolo')),
            ],
            options={
                'verbose_name': 'Recomendação',
                'verbose_name_plural': 'Recomendações',
            },
        ),
        migrations.AddField(
            model_name='produtor',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
        migrations.AddField(
            model_name='cultura',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
