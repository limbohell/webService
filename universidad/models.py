# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    curp = models.CharField(max_length=18)
    f_nacimiento = models.DateField()
    masculino = 'Masculino'
    femenino = 'Femenino'
    SEXO_CHOICES = (
        (masculino, 'Masculino'),
        (femenino, 'Femenino'),
    )
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=15)
    director = 'Director'
    secretario = 'Secretario'
    profesor = 'Profesor'
    estudiante = 'Estudiante'
    TIPO_CHOICES = (
        (director, 'Director'),
        (secretario, 'Secretario'),
        (profesor, 'Profesor'),
        (estudiante, 'Estudiante'),
    )
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=15)

    def __str__(self):
        return '%s %s' % (self.nickname, self.nombre)

class Notificacion(models.Model):
    mensaje = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.BooleanField(default=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (str(self.fecha), self.persona)

class Director(models.Model):
    rfc = models.CharField(max_length=20, unique=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.rfc, self.persona)

class Secretaria(models.Model):
    rfc = models.CharField(max_length=20, unique=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.rfc, self.persona)

class Profesor(models.Model):
    rfc = models.CharField(max_length=20, unique=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.rfc, self.persona)

class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=30, unique=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombre, self.clave)

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=30, unique=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombre, self.clave)

class Semestre(models.Model):
    primero = 'Primero'
    segundo = 'Segundo'
    tercero = 'Tercero'
    cuarto = 'Cuarto'
    quinto = 'Quinto'
    sexto = 'Sexto'
    septimo = 'Septimo'
    octavo = 'Octavo'
    noveno = 'Noveno'
    decimo = 'Decimo'
    undecimo = 'Undécimo'
    decimosegundo = 'Decimosegundo'

    SEMESTRE_CHOICES = (
        (primero, 'Primero'),
        (segundo, 'Segundo'),
        (tercero, 'Tercero'),
        (cuarto, 'Primero'),
        (quinto, 'Quinto'),
        (sexto, 'Sexto'),
        (septimo, 'Septimo'),
        (octavo, 'Octavo'),
        (noveno, 'Noveno'),
        (decimo, 'Decimo'),
        (undecimo, 'Undécimo'),
        (decimosegundo, 'Decimosegundo'),
    )

    descripcion = models.CharField(choices=SEMESTRE_CHOICES, max_length=15)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.descripcion, self.carrera)

class Grupo(models.Model):
    clave = models.CharField(max_length=20, unique=True)
    periodo_escolar = models.CharField(max_length=20, unique=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.clave, self.semestre)

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    clave = models.CharField(max_length=30, unique=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.clave, self.semestre)

class Alumno(models.Model):
    matricula = models.CharField(max_length=50, unique=True)
    estado = models.BooleanField(default=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.matricula, self.persona)

class ProfesorHasMateria(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.profesor, self.materia)

class Calificacion(models.Model):
    promedio = models.DecimalField(decimal_places=2, max_digits=4)
    profesorHasMateria = models.ForeignKey(ProfesorHasMateria, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (str(self.promedio), self.profesorHasMateria)

class CalificacionCatalogo(models.Model):
    promedio = models.DecimalField(decimal_places=2, max_digits=4)

    PRIMER_PERIODO = 0.2
    SEGUNDO_PERIODO = 0.2
    TERCER_PERIODO = 0.2
    ORDINARIO = 0.4

    TIPO_CHOICES = (
        (PRIMER_PERIODO, 'Primer Periodo'),
        (SEGUNDO_PERIODO, 'Segundo Periodo'),
        (TERCER_PERIODO, 'Tercer Periodo'),
        (ORDINARIO, 'Ordinario'),
    )

    tipo = models.DecimalField(choices=TIPO_CHOICES, decimal_places=2, max_digits=4)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.tipo, str(self.calificacion))
