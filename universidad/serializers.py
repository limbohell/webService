from rest_framework import serializers
from . import models

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = ('id', 'nickname', 'password', 'nombre', 'apellido_paterno',
                    'apellido_materno', 'apellido_paterno', 'curp',
                    'f_nacimiento', 'sexo', 'tipo')

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notificacion
        fields = ('id', 'mensaje', 'fecha', 'estado', 'persona')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ('id','rfc','persona')

class SecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Secretaria
        fields = ('id', 'rfc','persona','director')

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profesor
        fields = ('id', 'rfc', 'persona')

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrera
        fields = ('id', 'nombre', 'clave', 'escuela')

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Semestre
        fields = ('id','descripcion', 'carrera')

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grupo
        fields = ('id', 'clave', 'periodo_escolar', 'semestre')

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        fields = ('id', 'nombre', 'clave', 'semestre')

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alumno
        fields = ('id', 'matricula', 'estado', 'grupo', 'persona')

class ProfesorHasMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfesorHasMateria
        fields = ('id', 'profesor', 'materia')

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calificacion
        fields = ('id', 'promedio', 'profesorHasMateria')

class CalificacionCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CalificacionCatalogo
        fields = ('id', 'promedio', 'tipo', 'calificacion')
