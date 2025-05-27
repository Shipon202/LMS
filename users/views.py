from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import Userserializer
# Create your views here.
# @api_view(['GET','POST'])

# def user_list_create(request):
#     if request.method == 'GET':
#         if not request.user.is_authenticated :
#             return Response({'details' : 'You are not authenticated'}, status=401)
#         if request.user.role == 'admin':
#             users = User.objects.all()
#         else:
#             users = User.objects.filter(id=request.user.id)
#         serializer = Userserializer(users, many=True)
#         return Response(serializer.data)
#     elif request.method =='POST':
#         serializer = Userserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)








@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({'details': 'You are not authenticated'}, status=401)
        if request.user.role == 'admin':
            users = User.objects.all()
        else:
            users = User.objects.filter(id=request.user.id)
        serializer = Userserializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
