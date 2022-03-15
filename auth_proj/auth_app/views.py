from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def public_view(request):
    return Response({'message': 'this is a public view'})


@api_view(['GET'])
def private_view(request):
    return Response({'message': 'this is a private view'})
