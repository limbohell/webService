# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=50, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promedio', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='CalificacionCatalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promedio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tipo', models.DecimalField(choices=[(0.2, 'Primer Periodo'), (0.2, 'Segundo Periodo'), (0.2, 'Tercer Periodo'), (0.4, 'Ordinario')], decimal_places=2, max_digits=4)),
                ('calificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Calificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('clave', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('clave', models.CharField(max_length=30, unique=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=20, unique=True)),
                ('periodo_escolar', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('curp', models.CharField(max_length=18)),
                ('f_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=15)),
                ('tipo', models.CharField(choices=[('Director', 'Director'), ('Secretario', 'Secretario'), ('Profesor', 'Profesor'), ('Estudiante', 'Estudiante')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=20, unique=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='universidad.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='ProfesorHasMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Materia')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=20, unique=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Director')),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='universidad.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(choices=[('Primero', 'Primero'), ('Segundo', 'Segundo'), ('Tercero', 'Tercero'), ('Cuarto', 'Primero'), ('Quinto', 'Quinto'), ('Sexto', 'Sexto'), ('Septimo', 'Septimo'), ('Octavo', 'Octavo'), ('Noveno', 'Noveno'), ('Decimo', 'Decimo'), ('Und\xe9cimo', 'Und\xe9cimo'), ('Decimosegundo', 'Decimosegundo')], max_length=15)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Carrera')),
            ],
        ),
        migrations.AddField(
            model_name='notificacion',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Persona'),
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Semestre'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Semestre'),
        ),
        migrations.AddField(
            model_name='director',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='universidad.Persona'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Escuela'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='profesorHasMateria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.ProfesorHasMateria'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Grupo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='universidad.Persona'),
        ),
    ]