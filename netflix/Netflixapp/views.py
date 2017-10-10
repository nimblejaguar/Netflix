from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelDataSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Netflix, Payment, contact, Movies, Genre, FAQ, waystowatch, Shows, Customer
from .serializers import NetflixSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_netflix(request, pk):
    try:
        netflix = Netflix.objects.get(pk=pk)
    except Netflix.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single netflix
    if request.method == 'GET':
        return Response({})
    # delete a single netflix
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single netflix
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_Netflixapp(request):
    # get all Netflixapp
    if request.method == 'GET':
        return Response({})
    # insert a new record for a Netflix
    elif request.method == 'POST':
        return Response({})
