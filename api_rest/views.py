from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

#buscar todos os usuários
@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) #'many' significa que é uma queryset
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


#buscar usuário por primary_key(no caso a pk é o nickname)
@api_view(['GET'])
def get_user_by_nick(request, nick):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=nick)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


#criar novo usuário
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


#atualizar usuário existente
@api_view(['PUT'])
def update_user(request, nick):
    if request.method == 'PUT':

        try:
            user = User.objects.get(pk=nick)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                
        return Response(status=status.HTTP_400_BAD_REQUEST)


#deletar usuário existente
@api_view(['DELETE'])
def delete_user(request, nick):
    if request.method == 'DELETE':

        try:
            user_to_delete = User.objects.get(pk=nick)
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        



