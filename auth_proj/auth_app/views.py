import http

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import base64


from django.contrib.auth import authenticate


@api_view(['GET'])
def public_view(request):
    return Response({'message': 'this is a public view'})

# @api_view(['GET'])
# def private_view(request):
#     print(request.headers)
#     message_bytes = base64.b64decode(request.headers['Authorization'].replace("Basic ", ""))
#     message = message_bytes.decode('ascii')
#     print(message)
#     username, password = message.split(":")
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         # A backend authenticated the credentials
#         pass
#     else:
#         # No backend authenticated the credentials
#         return Response(status=http.HTTPStatus.UNAUTHORIZED)
#
#     return Response({'message': 'this is a private view'})


"""
Option 1: manual implementation
"""
# @api_view(['GET'])
# def private_view(request):
#     print(request.headers)
#     message_bytes = base64.b64decode(request.headers['Authorization'].replace("Basic ", ""))
#     message = message_bytes.decode('ascii')
#     print(message)
#     username, password = message.split(":")
#
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         # A backend authenticated the credentials
#         pass
#     else:
#         # No backend authenticated the credentials
#         return Response(status=http.HTTPStatus.UNAUTHORIZED)
#     return Response({'message': 'this is a private view'})


# """
# Option 2: using decorators
# """
#TokenAuthentication, BasicAuthentication
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def private_view(request):
    print(request.user)
    return Response({'message': 'this is a private view'})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sign_out(request):
    Token.objects.filter(key=request.auth.key).delete()
    return Response()