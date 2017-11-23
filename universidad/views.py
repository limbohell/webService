# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from universidad.models import *
from universidad.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PersonaList(APIView):
    def get(self, request, format=None):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaDetail(APIView):
    def get_object(self, nickname):
        try:
            return Persona.objects.get(nickname=nickname)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, nickname, format=None):
        persona = self.get_object(nickname=nickname)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, nickname, format=None):
        persona = self.get_object(nickname=nickname)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, nickname, format=None):
        persona = self.get_object(nickname=nickname)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
