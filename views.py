from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from cookbook import models
from cookbook import serializers
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status


class ReceipeViewSet(generics.ListCreateAPIView):

    def get(self,request,format=None):
        queryset = models.Recipe.objects.all()
        serializer= serializers.ReceipeSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = serializers.ReceipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(seriializer.error,status=status.HTTP_400_BAD_REQUEST)
    
        
    def get_object(self,pk):
        try:
            return models.Recipe.objects.get(pk=pk)
        except models.Recipe.DoesNotExist:
            raise Http404
        
    def put(self,request,pk):
        receipe=self.get_object(pk)
        serializer = serializers.ReceipeSerializer(receipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk):
        receipe=self.get_object(pk)
        receipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


    

        
    
