# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.Alumno)
admin.site.register(models.Calificacion)
admin.site.register(models.CalificacionCatalogo)
admin.site.register(models.Carrera)
admin.site.register(models.Director)
admin.site.register(models.Escuela)
admin.site.register(models.Grupo)
admin.site.register(models.Materia)
admin.site.register(models.Notificacion)
admin.site.register(models.Persona)
admin.site.register(models.Profesor)
admin.site.register(models.ProfesorHasMateria)
admin.site.register(models.Secretaria)
admin.site.register(models.Semestre)
# Register your models here.
