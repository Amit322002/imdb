from django.shortcuts import render,HttpResponse
from .models import WatchList,StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST','PUT','DELETE'])
def movie_list(request):
    if request.method=='GET':
        movies=WatchList.objects.all()
        serialized=WatchListSerializer(movies, many=True)
        return Response(serialized.data)
    
    elif request.method == 'POST':
        _data=request.data
        serialized=WatchListSerializer(data=_data)
        if serialized.is_valid():
             serialized.save()
             return Response(serialized.data , status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
    
@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = WatchListSerializer(movie)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized = WatchListSerializer(movie, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST','PUT','DELETE'])
def stream_list(request):
    if request.method=='GET':
        streamer=StreamPlatform.objects.all()
        serialized=StreamPlatformSerializer(streamer, many=True)
        return Response(serialized.data)
    
    elif request.method=='POST':
        _data=request.data
        serialized=StreamPlatformSerializer(data=_data)
        if serialized.is_valid():
             serialized.save()
             return Response(serialized.data , status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def stream_detail(request, pk):
    try:
        stream = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
        return Response({"error": "Streamer not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized =StreamPlatformSerializer(stream)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized =StreamPlatformSerializer(stream, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
